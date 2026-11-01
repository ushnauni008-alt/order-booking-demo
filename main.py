from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import uuid
import time
import random

app = FastAPI(
    title="Order Booking Demo",
    version="1.0"
)
orders = []

class Order(BaseModel):
    customer_name: str
    product_name: str
    quantity: int
    price: float

@app.get("/")
def home():
    return {
        "message": "Order Booking Application is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/order")
def create_order(order: Order):

    if random.random() < 0.9:
        time.sleep(20)

    order_id = str(uuid.uuid4())
    total_amount = order.quantity * order.price

    new_order = {
        "order_id": order_id,
        "customer_name": order.customer_name,
        "product_name": order.product_name,
        "quantity": order.quantity,
        "price": order.price,
        "total_amount": total_amount,
        "order_status": "BOOKED",
        "created_at": datetime.utcnow().isoformat()
    }

    orders.append(new_order)

    return new_order

@app.get("/orders")
def get_orders():
    return {
        "total_orders": len(orders),
        "orders": orders
    }
    

    return {
        "order_id": order_id,
        "customer_name": order.customer_name,
        "product_name": order.product_name,
        "quantity": order.quantity,
        "order_status": "BOOKED",
        "created_at": datetime.utcnow().isoformat()
    }