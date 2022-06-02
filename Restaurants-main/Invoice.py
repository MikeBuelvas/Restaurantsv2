import Client, Order

class Invoice:
    def __init__(
            self,
            id: int,
            client: Client,
            order: Order       
    ) -> None:
        self.id = id
        self.client = client
        self.order = order