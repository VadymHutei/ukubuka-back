from flask import Flask
from flask_restful import Api

from resources import (
    Language,
    Menu,
    MenuItem,
    Category,
    Product,
    SKU,
    Characteristic,
    Currency
)


app = Flask(__name__)
api = Api(app)

api.add_resource(Language, '/languages')
api.add_resource(Menu, '/menus')
api.add_resource(MenuItem, '/menus/items')
api.add_resource(Category, '/categories')
api.add_resource(Product, '/products')
api.add_resource(SKU, '/sku')
api.add_resource(Characteristic, '/characteristics')
api.add_resource(Currency, '/currencies')


@app.route('/', methods=['GET'])
def main():
    return 'Back works!'
