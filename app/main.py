from flask import Flask
from flask_restful import Api

from resources import (
    Languages,
    Menus,
    MenuItems,
    Categories,
    Products,
    Sku,
    Characteristics,
    Currencies
)


app = Flask(__name__)
api = Api(app)

api.add_resource(Languages, '/languages')
api.add_resource(Menus, '/menus')
api.add_resource(MenuItems, '/menus/items')
api.add_resource(Categories, '/categories')
api.add_resource(Products, '/products')
api.add_resource(Sku, '/sku')
api.add_resource(Characteristics, '/characteristics')
api.add_resource(Currencies, '/currencies')

@app.route('/', methods=['GET'])
def main():
    return 'Back works!'
