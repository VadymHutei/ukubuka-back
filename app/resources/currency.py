from flask import jsonify
from flask_restful import Resource


class Currency(Resource):

    def get(self):
        return jsonify(
            {}
        )
