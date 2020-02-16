from flask import jsonify

from core import Resource
from core.validator import (
    common as v_common,
    menu as v_menu
)
from repositories import MenuRepo


class Menu(Resource):

    def __init__(self):
        super().__init__()
        self._parser.add_argument(
            'language',
            required=True,
            location='headers'
        )
        self._parser.add_argument(
            'active',
            dest='is_active',
            choices=('y', 'n'),
            case_sensitive=False,
            store_missing=False,
            location='args'
        )
        self._parser.add_argument(
            'order',
            choices=('asc', 'desc'),
            case_sensitive=False,
            store_missing=False,
            location='args'
        )
        self._parser.add_argument(
            'order_by',
            action='append',
            store_missing=False,
            location='args'
        )
        self._transform_methods = {
            'order_by': lambda x: [tuple(y.split('-')[-2:]) for y in x]
        }
        self._validation_methods = {
            'language': v_common.languageCode,
            'is_active': v_common.active,
            'order': v_common.orderDirection,
            'order_by': (
                v_common.fieldName,
                v_common.orderDirection
            )
        }

    def get(self):
        self._parseArguments()
        self._transformArguments()
        self._validateArguments()
        repo = MenuRepo()
        result = repo.getMenus(self._getArguments())
        return jsonify(result)

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass


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
