from flask import jsonify
from flask_restful import reqparse, abort

from core import Resource, validator
from repositories import MenuRepo


class Menus(Resource):

    def _setArguments(self) -> None:
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='args')
        parser.add_argument('alias', location='args')
        parser.add_argument('active', location='args')
        parser.add_argument('order', location='args')
        parser.add_argument('language', location='headers')
        self._args = parser.parse_args()

    def _validArguments(self) -> None:
        validFuncs = {
            'id': validator.menuID,
            'alias': validator.menuAlias,
            'active': validator.active,
            'order': validator.orderDirection,
            'language': validator.languageCode
        }
        forDeleting = []
        for key, value in self._args.items():
            if value is None:
                forDeleting.append(key)
                continue
            if key in validFuncs:
                if not validFuncs[key](value):
                    abort(400, message=f'Wrong {key}')
                continue
            else:
                forDeleting.append(key)
        for key in forDeleting:
            del self._args[key]

    def get(self):
        self._setArguments()
        self._validArguments()
        params = self._getParams('active', 'order', 'language')
        repo = MenuRepo()
        getDataMethods = {
            'id': repo.getMenuByID,
            'alias': repo.getMenuByAlias
        }
        for arg in getDataMethods:
            if self._argsContains(arg):
                data = getDataMethods[arg](self._getArg(arg), **params)
                break
            abort(400, message='Menu ID or alias are required')

        result = self._getMenuStructure(data)

        return jsonify(result)

    def _getMenuStructure(self, items) -> dict:
        return {}
