from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return 'Back works!'

@app.route('/categories/', methods=['GET'])
def categories():
    return 'Categories works!'

@app.route('/products/', methods=['GET'])
def products():
    return 'Products works!'

@app.route('/sku/', methods=['GET'])
def sku():
    return 'Sku works!'

@app.route('/characteristics/', methods=['GET'])
def characteristics():
    return 'Characteristics works!'

@app.route('/users/', methods=['GET'])
def users():
    return 'Users works!'

@app.route('/menus/', methods=['GET'])
def menus():
    return 'Menus works!'