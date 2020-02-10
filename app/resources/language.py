from flask import jsonify
from flask_restful import Resource


class Language(Resource):

    def get(self):
        return jsonify(
            {}
        )
