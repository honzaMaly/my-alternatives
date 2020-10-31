"""Recommendation Resources - Endpoints to make recommendations"""

from flask_restplus import fields, Resource, Namespace

from database import kaava_karlin
from model import CategoryEnum, RecommendationTypeEnum
from model.profiles import Profile
from model.recommendations import Recommendation

# create namespace
recommendations_api = Namespace('recommendations', description='Recommendation related operations')

# create models for serializations & documentation

# recommendation item
recommendation_model = recommendations_api.model('Recommendation', {
    'place': fields.String(attribute=lambda x: x.place.location_id),
    'user': fields.String(attribute=lambda x: x.user.user_id),
    'category': fields.String(attribute=lambda x: x.category.name),
    'recommendation_type': fields.String(attribute=lambda x: x.recommendation_type.name),
})

# list of recommendations
recommendation_list_model = recommendations_api.model('RecommendationList', {
    'recommendations': fields.List(fields.Nested(recommendation_model)),
})


@recommendations_api.route("/<string:user_id>")
@recommendations_api.param('user_id', 'ID of the user')
@recommendations_api.response(404, 'User not found')
class RecommendationResource(Resource):

    @recommendations_api.marshal_with(recommendation_list_model)
    def get(self, user_id: str):

        # TODO - implement

        # create dummy user
        dummy_profile = Profile(user_id)

        # create dummy recommendations
        return {
            'recommendations': [
                Recommendation(
                    place=kaava_karlin,
                    user=dummy_profile,
                    category=CategoryEnum.coffee,
                    recommendation_type=RecommendationTypeEnum.frequency
                )
            ]
        }
