from flask import jsonify
from flask_restful import Resource


class Characteristic(Resource):

    def get(self):
        return jsonify(
            {}
        )
