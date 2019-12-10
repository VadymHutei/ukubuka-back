from flask import jsonify
from flask_restful import Resource, reqparse


class Menus(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('parent', type=int, location='args')
        parser.add_argument('alias', location='args')
        parser.add_argument('active', location='args')
        parser.add_argument('order', location='args')
        parser.add_argument('language', location='headers')

        args = parser.parse_args()

        return jsonify(
            [
                {
                    'id': 2,
                    'name': 'Квіти',
                    'parent': 1,
                    'link': '/flowers/',
                    'order': 100
                },
                {
                    'id': 4,
                    'name': 'Букети',
                    'parent': 2,
                    'link': '/flowers/bouquets/',
                    'order': 10
                },
                {
                    'id': 5,
                    'name': 'Рослини',
                    'parent': 2,
                    'link': '/flowers/plants/',
                    'order': 20
                },
                {
                    'id': 3,
                    'name': 'Меблі',
                    'parent': 1,
                    'link': '/furniture/',
                    'order': 100
                }
            ]
        )
