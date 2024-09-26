from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = [
        {"order_id": 1, "item": "Laptop", "price": 1200},
        {"order_id": 2, "item": "Phone", "price": 800}
    ]
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
