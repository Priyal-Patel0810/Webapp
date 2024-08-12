from flask import Flask, jsonify
from flask_cors import CORS

# Initialize your app
app = Flask(__name__)
CORS(app)

# Sample product data
products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Smartphone", "price": 599.99},
    {"name": "Tablet", "price": 399.99},
    {"name": "Headphones", "price": 199.99},
    {"name": "Smartwatch", "price": 249.99},
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({"products": products})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
