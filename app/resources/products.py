from flask import jsonify
from flask_restful import Resource


class Products(Resource):

    def get(self):
        return jsonify(
            {}
        )
