from typing import Optional

class Order:
    def __init__(
            self,
            order_status: bool,
            table: int,
            saucers: Optional[list] = None,  
            drinks: Optional[list] = None               
    ) -> None:
        self.saucers = saucers
        self.drinks = drinks
        self.order_status = order_status
        self.table = table