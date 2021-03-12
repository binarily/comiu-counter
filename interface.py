from service import Order, CounterService


class DummyInterface:
    def __init__(self):
        self.service = CounterService(self)

    def print_order(self, order: Order):
        result = ""
        result += f"Order #{order.id}\n"
        for beverage in order.elements:
            result += f"Ordered: {beverage.beverage.name} x {beverage.quantity}\n"
        if order.colour is None:
            result += f"Order is prepared, no colour yet.\n"
        else:
            result += (f"Order is ready, deliver to colour {order.colour.colour} "
                       f"in segment {order.colour.segment}")
        return result

    def handle_ready(self, order_id: int):
        self.service.handle_ready_action(order_id)

    def handle_done(self, order_id: int):
        self.service.handle_done_action(order_id)

    def list_entries(self):
        return self.service.print_all_orders()
