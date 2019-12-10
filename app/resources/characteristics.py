from flask import jsonify
from flask_restful import Resource


class Characteristics(Resource):

    def get(self):
        return jsonify(
            {}
        )
