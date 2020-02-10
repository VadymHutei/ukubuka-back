from flask import jsonify
from flask_restful import Resource


class Product(Resource):

    def get(self):
        return jsonify(
            {}
        )
