from flask import jsonify
from flask_restful import Resource


class MenuItems(Resource):

    def get(self):
        return jsonify(
            {}
        )
