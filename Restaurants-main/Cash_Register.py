import pickle
import Employee,Invoice, Client, Order

class Cash_Register():
    def __init__(
            self,
            balance: float,
            admin: Employee,
            id_admin: str,
            sales: list        
    ) -> None:
        self.balance = balance
        self.admin = admin
        self.id_admin = id_admin
        self.sales = sales
    
    def gen_invoice(
            self,
            id: int,
            client: Client,
            order: Order
        ) -> Invoice:                    
            invoice = Invoice(id,client,order)
            for saucer in invoice.order.saucers:
                invoice.total += saucer.price

            for drink in invoice.order.drinks:
                invoice.total += drink.price
            self.balance += invoice.total
            self.sales.append(invoice)
            self.save_bs()
            return invoice

    def save_bs(self) -> None:
        archive_balance = open("archive_balance","wb")
        archive_sales = open("archive_sales","wb")
        pickle.dump(self.balance, archive_balance)
        pickle.dump(self.sales, archive_sales)
        archive_balance.close()
        archive_sales.close()
        del(archive_balance)
        del(archive_sales)
