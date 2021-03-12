from fastapi import FastAPI

from interface import DummyInterface
from requests import OrderRequest

app = FastAPI()
interface = DummyInterface()


@app.post("/order/incoming")
def order_incoming(request: OrderRequest):
    interface.service.handle_new_order(request)
    return {
        "orderId": request.orderId,
        "status": "OK"
    }


@app.get("/interface/list")
def print_entries():
    return interface.list_entries()


@app.get("/interface/ready/{order_id}")
def ready(order_id: int):
    interface.handle_ready(order_id)
    return interface.list_entries()


@app.get("/interface/done/{order_id}")
def ready(order_id: int):
    interface.handle_done(order_id)
    return interface.list_entries()
