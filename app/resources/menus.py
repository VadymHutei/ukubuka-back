from flask import jsonify
from flask_restful import Resource, reqparse, abort

from core import validator
from repositories import MenuRepo


class Menus(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('parent', type=int, location='args')
        parser.add_argument('alias', location='args')
        parser.add_argument('active', location='args')
        parser.add_argument('order', location='args')
        parser.add_argument('language', location='headers')
        args = parser.parse_args()

        param = {}
        if args['active'] is not None and validator.active(args['active']):
            param['active'] = args['active'].upper()
        if args['order'] is not None and validator.orderDirection(args['order']):
            param['order'] = args['order'].upper()
        if args['language'] is not None and validator.languageCode(args['language']):
            param['language'] = args['language'].lower()

        repo = MenuRepo()
        if args['parent'] is not None and validator.menuID(args['parent']):
            data = repo.getMenuByID(args['parent'], **param)
        elif args['alias'] is not None and validator.menuID(args['alias']):
            data = repo.getMenuByAlias(args['alias'], **param)
        else:
            abort(400, message='Menu ID or alias are required')

        result = self._getMenuStructure()

        return jsonify(result)

    def _getMenuStructure(self, items) -> dict:
        return {}
