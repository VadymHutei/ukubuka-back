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
                try:
                    data = getDataMethods[arg](self._getArg(arg), **params)
                except Exception:
                    abort(500)
                break
            abort(400, message='Menu ID or alias are required')

        data['items'] = self._getMenuStructure(data['items'])

        return jsonify(data)

    def _getMenuStructure(self, items) -> dict:
        result = []
        checked = []
        data_d = {}
        dependencies = {}
        for item in items:
            parent = item['parent']
            id_ = item['id']
            data_d[id_] = item
            if parent not in dependencies:
                dependencies[parent] = []
            dependencies[parent].append(id_)
        movement_counter = 1
        while movement_counter > 0:
            movement_counter = 0
            for id_ in data_d:
                item = data_d[id_]
                parent = item['parent']
                if id_ in checked:
                    continue
                if id_ in dependencies:
                    continue
                if parent in data_d:
                    if 'subitems' not in data_d[parent]:
                        data_d[parent]['subitems'] = []
                    data_d[parent]['subitems'].append(item)
                    dependencies[parent].remove(id_)
                    if not dependencies[parent]:
                        del dependencies[parent]
                else:
                    result.append(item)
                checked.append(id_)
                movement_counter += 1
        return result
