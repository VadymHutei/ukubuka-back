from flask import jsonify
from flask_restful import Resource


class Languages(Resource):

    def get(self):
        return jsonify(
            {}
        )
