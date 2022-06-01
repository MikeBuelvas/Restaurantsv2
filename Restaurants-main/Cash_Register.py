import Employee, Invoice, Order, Client

class Cash_Register():
    def __init__(
            self,
            balance: str,
            admin: Employee,
            id_admin: str        
    ) -> None:
        self.balance = balance
        self.admin = admin
        self.id_admin = id_admin
        self.sales = []

    def gen_invoice(
            self,
            id: int,
            client: Client,
            order: Order
    ) -> Invoice:
        invoice = Invoice(id,client,order)
        self.sales.append(invoice)