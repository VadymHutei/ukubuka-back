from flask import Flask
from flask_restful import Api

from resources import (
    Menus,
    MenuItems
)


app = Flask(__name__)
api = Api(app)

api.add_resource(Menus, '/menus')
api.add_resource(MenuItems, '/menus/items')

@app.route('/', methods=['GET'])
def main():
    return 'Back works!'
