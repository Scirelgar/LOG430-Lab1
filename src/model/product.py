class Product:
    def __init__(
        self,
        product_id: int,
        name: str,
        category: str,
        price: float,
        stock_quantity: int = 0,
    ):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self) -> str:
        return f"Product ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock Quantity: {self.stock_quantity}"

    @property
    def state(self) -> str:
        if self.stock_quantity > 0:
            return "In Stock"
        elif self.stock_quantity == 0:
            return "Out of Stock"
        else:
            return "Invalid Stock Quantity"
