class Order:
    def __init__(self, id, product_id, quantity):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity

# Пример данных
orders = [
    Order(1, 1, 2),
    Order(2, 2, 1)
]
