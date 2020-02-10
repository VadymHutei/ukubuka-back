from flask import jsonify
from flask_restful import reqparse, abort

from core import Resource, validator
from repositories import MenuRepo


class Menu(Resource):

    def _setArguments(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='args')
        parser.add_argument('alias', location='args')
        parser.add_argument('active', location='args')
        parser.add_argument('order', location='args')
        parser.add_argument('language', location='headers')
        self._args = parser.parse_args()

    def get(self):
        self._setArguments()
        validFuncs = {
            'id': validator.menu.menuID,
            'alias': validator.menu.menuAlias,
            'active': validator.common.active,
            'order': validator.common.orderDirection,
            'language': validator.common.languageCode
        }
        self._validArguments(validFuncs)
        params = self._getParams('active', 'order', 'language')
        repo = MenuRepo()
        getDataMethods = {
            'id': repo.getMenuByID,
            'alias': repo.getMenuByAlias
        }
        for arg in getDataMethods:
            if self._hasArg(arg):
                try:
                    data = getDataMethods[arg](self._getArg(arg), **params)
                    data['items'] = self._getMenuStructure(data['items'])
                    return jsonify(data)
                except Exception:
                    abort(500)
        abort(400, message='Menu ID or alias are required')

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
