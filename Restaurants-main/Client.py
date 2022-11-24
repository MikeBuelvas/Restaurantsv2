import Person

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
        
    def client_payment(self, status: bool) -> None:
                self.bill_status = status
            

    
