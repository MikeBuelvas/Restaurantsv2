import Person, Order

class Employee(Person):
    def __init__(
            self,
            name: str,
            id: int,           
            age: int,
            salary: float,
            job: str                 
    ) -> None:
        super().__init__(
            name,
            id
        )
        self.age = age
        self.salary = salary
        self.job = job

    def create_order(
                self,
                nsaucers: int,
                ndrinks: int,
                order_status: bool,
                table: int
            ) -> Order:
            self.nsaucers = nsaucers
            self.ndrinks = ndrinks
            self.order_status = order_status
            self.table = table
            self.saucers = []
            self.drinks = []

            for x in range(nsaucers):
                self.saucer = input("Digite plato: ")
                self.saucers.append(self.saucer)

            for x in range(ndrinks):
                self.drink = input("Digite Bebida: ")
                self.drinks.append(self.drink)

            self.order = Order(self.order_status, self.table, self.saucers, self.drinks)
            
            return self.order


    


