from flask import jsonify
from flask_restful import Resource


class MenuItems(Resource):
    '''

    ARGUMENT    DEFAULT VALUE   ALTERNATIVE VALUE
    structure   list            tree
    active      Y               N
    parent      None            <item_id>

    '''
    def get(self):
        return jsonify(
            {}
        )
