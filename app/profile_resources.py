"""Recommendation Resources - Endpoints to get profile data"""

from flask_restplus import fields, Resource, Namespace

from database import dummy_profile

# create namespace
profile_api = Namespace('profile', description='Profile related operations')

# profile item
profile_model = profile_api.model('Profile', {
    'user_id': fields.String,
    'name': fields.String,
    'profile_image_url': fields.String,
    'count_of_alternatives': fields.Integer(attribute='alternatives'),
    'rank': fields.String(attribute=lambda x: x.get_rank().name),
})


@profile_api.route("/<string:user_id>")
@profile_api.param('user_id', 'ID of the user')
@profile_api.response(404, 'User not found')
class ProfileResource(Resource):

    @profile_api.marshal_with(profile_model)
    def get(self, user_id: str):
        # TODO - implement
        return dummy_profile
