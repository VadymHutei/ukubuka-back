from flask import jsonify
from flask_restful import Resource


class Currencies(Resource):

    def get(self):
        return jsonify(
            {}
        )
