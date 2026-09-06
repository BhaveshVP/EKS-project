from fastapi import FastAPI

app = FastAPI(title="Products API")


products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 75000,
        "category": "Electronics"
    },
    {
        "id": 2,
        "name": "Mobile Phone",
        "price": 35000,
        "category": "Electronics"
    },
    {
        "id": 3,
        "name": "Keyboard",
        "price": 2500,
        "category": "Accessories"
    },
    {
        "id": 4,
        "name": "Mouse",
        "price": 1200,
        "category": "Accessories"
    }
]


@app.get("/")
def home():
    return {
        "service": "products-api",
        "message": "Products API is running"
    }


@app.get("/api/products")
def get_products():
    return products


@app.get("/api/products/{product_id}")
def get_product(product_id: int):

    for product in products:
        if product["id"] == product_id:
            return product

    return {
        "error": "Product not found"
    }
