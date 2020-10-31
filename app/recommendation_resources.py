"""Recommendation Resources - Endpoints to get recommendations"""
from flask import request
from flask_restplus import fields, Resource, Namespace

from database import dummy_recommendation

# create namespace
recommendation_api = Namespace('recommendation', description='Recommendation related operations')

# recommendation item
recommendation_model = recommendation_api.model('Recommendation', {
    'place': fields.String(attribute=lambda x: x.place.location_id),
    'recommendation_id': fields.String,
    'user': fields.String(attribute=lambda x: x.user.user_id),
    'category': fields.String(attribute=lambda x: x.category.name),
    'recommendation_type': fields.String(attribute=lambda x: x.recommendation_type.name),
    'alternative_places': fields.List(
        fields.String, attribute=lambda x: [place.location_id for place in x.alternatives]),
})

# list of recommendations
recommendation_list_model = recommendation_api.model('RecommendationList', {
    'recommendations': fields.List(fields.Nested(recommendation_model)),
})


@recommendation_api.route("/<string:user_id>")
@recommendation_api.param('user_id', 'ID of the user')
@recommendation_api.param('lat', 'Latitude')
@recommendation_api.param('lon', 'Longitude')
@recommendation_api.response(404, 'User not found')
class RecommendationResource(Resource):

    @recommendation_api.marshal_with(recommendation_list_model)
    def get(self, user_id: str):
        # TODO - implement
        lat = request.args.get('lat', default=1, type=float)
        lon = request.args.get('lon', default=1, type=float)
        return {
            'recommendations': [
                dummy_recommendation
            ]
        }
