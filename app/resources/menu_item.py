from flask import jsonify
from flask_restful import Resource


class MenuItem(Resource):

    def get(self):
        return jsonify(
            {}
        )
