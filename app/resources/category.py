from flask import jsonify
from flask_restful import reqparse, abort

from core import Resource
from core.validator import common as v_common, menu as v_menu
from repositories import CategoryRepo


class Category(Resource):

    def get(self):
        parser = reqparse.RequestParser(trim=True, bundle_errors=False)
        parser.add_argument('language', required=True, location='headers')
        self._args = parser.parse_args()
        self._validArguments({
            'language': v_common.languageCode
        })
        params = self._getParams('language')
        repo = CategoryRepo()
        result = repo.getCategories(params)
        return jsonify(result)

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass

    def wdeget(self):
        self._setArguments()
        validFuncs = {
            'id': v_menu.menuID,
            'alias': v_menu.menuAlias,
            'active': v_common.active,
            'order': v_common.orderDirection,
            'language': v_common.languageCode
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