"""Definition of an API using 'Blueprint' so APIs can be versioned"""

from flask_restplus import Api

from app.recommendation_resources import recommendations_api

# initialization of the API
service_api: Api = Api(title='MyAlternatives API', version='1.0', doc='/doc/')

# add namespaces
service_api.add_namespace(recommendations_api)
