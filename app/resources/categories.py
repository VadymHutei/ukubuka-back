from flask import jsonify
from flask_restful import Resource


class Categories(Resource):

    def get(self):
        return jsonify(
            {}
        )
