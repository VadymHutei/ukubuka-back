from flask import Flask
from flask_restful import Api

from resources import (
    Category,
    Product,
    Menu
)


app = Flask(__name__)
api = Api(app)

api.add_resource(Category, '/categories')
api.add_resource(Product, '/products')
api.add_resource(Menu, '/menus')


@app.route('/', methods=['GET'])
def main():
    return 'Back works!'
