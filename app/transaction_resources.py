"""Transaction Resources - Endpoints to post transactions"""
import json

from flask import request
from flask_restplus import fields, Resource, Namespace

# create namespace
transaction_api = Namespace('transaction', description='Transaction related operations')

# transaction item
transaction_model = transaction_api.model('Transaction', {
    'user_id': fields.String,
    'place_id': fields.String
})


@transaction_api.route('/')
class TransactionResource(Resource):

    # payload validation enabled
    @transaction_api.doc(body=transaction_model)
    @transaction_api.expect(transaction_model, validate=True)
    def post(self):
        # TODO - implement
        payload = json.loads(request.data)
        return payload['user_id']
