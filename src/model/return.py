class Return:
    def __init__(
        self,
        return_id: int,
        return_date: str,
        return_lines: list,
        total_amount: float = 0.0,
    ):
        self.return_id = return_id
        self.return_date = None
        self.return_lines: list[ReturnLine] = []
        self.total_amount = 0.0

    def __str__(self) -> str:
        return f"Return ID: {self.return_id}, Date: {self.return_date}, Total Amount: {self.total_amount}"


class ReturnLine:
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
