from apps.orders.models import OrderLine, Order


class OrderLineDto():
    def __init__(self, product_id,quantity):
        self.product_id = product_id
        self.quantity=quantity



class OrderDto():
    def __init__(self, order, lines ):
        self.lines = []
        self.order_id=order.id
        for line in lines:
            order_line_dto=OrderLineDto(line.product.id,line.quantity)
            self.lines.append(order_line_dto)



