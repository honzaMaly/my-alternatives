"""Definition of an API using 'Blueprint' so APIs can be versioned"""

from flask_restplus import Api

from app.place_resources import place_api
from app.profile_resources import profile_api
from app.recommendation_resources import recommendation_api
from app.transaction_resources import transaction_api

# initialization of the API
service_api: Api = Api(title='MyAlternatives API', version='1.0', doc='/doc/')

# add namespaces
service_api.add_namespace(recommendation_api)
service_api.add_namespace(profile_api)
service_api.add_namespace(place_api)
service_api.add_namespace(transaction_api)
