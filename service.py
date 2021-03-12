from typing import List, Optional

from pydantic.dataclasses import dataclass

from requests import OrderRequest
from swagger_client import OrderControllerApi, OrderStatusResponse, OrderId, OrderColourResponse


@dataclass
class Beverage:
    name: str
    price: float
    sku: int
    available: bool  # Future-proofing for eventual checks


@dataclass
class BeverageWithQuantity:
    beverage: Beverage
    quantity: int


@dataclass
class ColourWithSegment:
    colour: int
    segment: int


@dataclass
class Order:
    id: int
    elements: List[BeverageWithQuantity]
    colour: Optional[ColourWithSegment] = None


class CounterService:
    server_api: OrderControllerApi
    device_id = 2

    def __init__(self, interface):
        from interface import DummyInterface
        self.orders: List[Order] = list()
        self.beverages: List[Beverage] = list()
        self.interface: DummyInterface = interface
        self.server_api = OrderControllerApi()

        # Testing set-up
        self.beverages.append(Beverage("Carlsberg", 12.0, 11, True))
        self.beverages.append(Beverage("Tuborg", 12.0, 12, True))
        self.beverages.append(Beverage("Okocim", 15.0, 13, True))
        self.beverages.append(Beverage("Desperados", 15.0, 14, True))
        self.beverages.append(Beverage("Sommersby", 10.0, 15, True))
        self.beverages.append(Beverage("Kronenburg", 15.0, 16, True))
        self.beverages.append(Beverage("Kustosz", 20.0, 17, True))
        self.beverages.append(Beverage("Grolsch", 12.0, 18, True))

    def print_all_orders(self):
        result = list()
        for order in self.orders:
            result.append(self.interface.print_order(order))
        return result

    def handle_new_order(self, order: OrderRequest):
        local_order = Order(
            id=order.orderId.id,
            elements=list()
        )
        local_order.id = order.orderId.id
        local_order.elements = list()
        for element in order.elements:
            local_bev = BeverageWithQuantity(
                beverage=next((x for x in self.beverages if x.sku == element.sku)),
                quantity=element.quantity
            )
            local_order.elements.append(local_bev)
        self.orders.append(local_order)

    def handle_ready_action(self, order_id: int):
        # Turn order into request
        current_order = next((x for x in self.orders if x.id == order_id), None)
        if current_order is None:
            return
        order_request = OrderId(id=current_order.id)
        # Send request with proper data to server
        response: OrderColourResponse = self.server_api.ready_using_post(self.device_id, order_request)
        if response.status == "OK":
            local_colour = ColourWithSegment(
                colour = response.colour.colour,
                segment = response.colour.segment
            )
            current_order.colour = local_colour

    def handle_done_action(self, order_id: int):
        # Turn order into request
        current_order = next((x for x in self.orders if x.id == order_id), None)
        if current_order is None:
            return
        order_request = OrderId(id=current_order.id)
        # Send request with proper data to server
        response: OrderStatusResponse = self.server_api.done_using_post(self.device_id, order_request)
        if response.status == "OK":
            self.orders.remove(current_order)
