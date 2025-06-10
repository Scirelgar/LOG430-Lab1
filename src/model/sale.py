class Sale:
    def __init__(
        self,
        sale_id: int,
        sale_date: str,
        sale_lines: list,
        total_amount: float = 0.0,
    ):
        self.sale_id = sale_id
        self.sale_date = None
        self.sale_lines: list[SaleLine] = []
        self.total_amount = 0.0

    def __str__(self) -> str:
        return f"Sale ID: {self.sale_id}, Date: {self.sale_date}, Total Amount: {self.total_amount}"


class SaleLine:
    def __init__(
        self,
        product_id: int,
        quantity: int,
    ):

        self.product_id = product_id
        self.unit_price = 0.0
        self.quantity = quantity

    def __str__(self) -> str:
        return f"Product ID: {self.product_id}, Quantity: {self.quantity}, Total Price: {self.total_price}"

    @property
    def total_price(self) -> float:
        return self.quantity * self.unit_price
