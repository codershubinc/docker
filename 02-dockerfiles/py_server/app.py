from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
PORT = 8080

# In-memory data store for demonstration purposes
products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Keyboard", "price": 75},
    {"id": 3, "name": "Mouse", "price": 25},
]
next_id = 4

@app.route('/')
def index():
    return "Hello from the Python Server!"

@app.route('/api/products', methods=['GET'])
def get_products():
    """Returns a list of all products."""
    return jsonify(products)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Returns a single product by its ID."""
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        raise NotFound(f"Product with ID {product_id} not found.")
    return jsonify(product)

@app.route('/api/products', methods=['POST'])
def create_product():
    """Creates a new product."""
    global next_id
    if not request.json or 'name' not in request.json or 'price' not in request.json:
        raise BadRequest("Request must be JSON and include 'name' and 'price' fields.")

    new_product = {
        'id': next_id,
        'name': request.json['name'],
        'price': request.json['price']
    }
    products.append(new_product)
    next_id += 1
    return jsonify(new_product), 201

if __name__ == '__main__':
    # Use 0.0.0.0 to make the server accessible from outside the container
    app.run(host='0.0.0.0', port=PORT, debug=True)
