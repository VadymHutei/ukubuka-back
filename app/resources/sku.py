from flask import jsonify
from flask_restful import Resource


class Sku(Resource):

    def get(self):
        return jsonify(
            {}
        )
