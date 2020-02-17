from flask import jsonify

from core import Resource
from core.validator import (
    common as v_common,
    category as v_category
)
from repositories import ProductRepo


class Product(Resource):

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
            'category',
            dest='category_id',
            action='append',
            store_missing=False,
            location='args'
        )
        self._transform_methods = {
            'category_id': lambda x: int(x)
        }
        self._validation_methods = {
            'language': v_common.languageCode,
            'is_active': v_common.active,
            'category_id': v_category.categoryID
        }

    def get(self):
        self._parseArguments()
        self._transformArguments()
        self._validateArguments()
        repo = ProductRepo()
        result = repo.getProducts(self._getArguments())
        return jsonify(result)

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
