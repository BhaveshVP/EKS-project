from fastapi import FastAPI

app = FastAPI(title="Orders API")


orders = [
    {
        "id": 1001,
        "customer": "Keyur",
        "product": "Laptop",
        "quantity": 1,
        "status": "CONFIRMED"
    },
    {
        "id": 1002,
        "customer": "Rahul",
        "product": "Mobile Phone",
        "quantity": 2,
        "status": "SHIPPED"
    },
    {
        "id": 1003,
        "customer": "Amit",
        "product": "Keyboard",
        "quantity": 1,
        "status": "DELIVERED"
    }
]


@app.get("/")
def home():
    return {
        "service": "orders-api",
        "message": "Orders API is running"
    }


@app.get("/api/orders")
def get_orders():
    return orders


@app.get("/api/orders/{order_id}")
def get_order(order_id: int):

    for order in orders:
        if order["id"] == order_id:
            return order

    return {
        "error": "Order not found"
    }
