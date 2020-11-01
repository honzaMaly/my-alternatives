"""Place Resources - Endpoints to get places"""

from flask_restplus import fields, Resource, Namespace

from database import PLACES_BY_ID

# create namespace
place_api = Namespace('place', description='Place related operations')

# review item
review_model = place_api.model('Review', {
    'user_name': fields.String,
    'review': fields.String,
    'rating': fields.Float,
    'created': fields.DateTime(dt_format='rfc822')
})

# recommendation item
place_model = place_api.model('Place', {
    'location_id': fields.String,
    'location_name': fields.String,
    'address': fields.String,
    'web': fields.String,
    'phone': fields.String,
    'story': fields.String,
    'lat': fields.Float,
    'lon': fields.Float,
    'rating': fields.Float,
    'reviews_count': fields.Integer(attribute='reviews_cnt'),
    'picture_urls': fields.List(fields.String, attribute=lambda x: list(x.picture_urls)),
    'categories': fields.List(fields.String, attribute=lambda x: list(cat.name for cat in x.categories)),
    'reviews': fields.List(fields.Nested(review_model)),
})


@place_api.route("/<string:location_id>")
@place_api.param('location_id', 'ID of the location')
@place_api.response(404, 'Location not found')
class PlaceResource(Resource):

    @place_api.marshal_with(place_model)
    def get(self, location_id: str):
        return PLACES_BY_ID.get(location_id)
