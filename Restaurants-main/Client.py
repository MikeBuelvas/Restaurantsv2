import Order, Invoice, Person

class Client(Person):
    def __init__(
            self,
            name: str,
            id: int      
    ) -> None:
        super().__init__(
            name,
            id
        )
        self.order_status = False
        self.bill_status = False

    def create_order(
            self,
            nsaucers: int,
            ndrinks: int,
            order_status: bool,
            table: int
        ) -> Order:
        saucers = []
        drinks = []

        for x in range(nsaucers):
            saucer = input("Digite plato: ")
            saucers.append(saucer)

        for x in range(ndrinks):
            drink = input("Digite Bebida: ")
            drinks.append(drink)

        order = Order(order_status, table, saucers, drinks)

        return order        

    def client_payment(self, status: bool) -> None:
        self.bill_status = status