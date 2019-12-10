from flask import jsonify
from flask_restful import Resource


class Menus(Resource):

    def get(self):
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
