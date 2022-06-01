from venv import create
import Cash_Register, Employee, Client


class Restaurant():
    def __init__(
            self,
            name: str,
            adress: str,
            phone_number: int        
    ) -> None:
        self.name = name
        self.adress = adress
        self.phone_number = phone_number
        self.admin = Employee("Mike Buelvas", 123456789,19,2555.4,"Administrador")
        self.cash_register = Cash_Register(0, self.admin, self.admin.id)
        self.employees = []
        self.clients = []

    def add_employee(
            self,
            name: str,
            id: int,
            age: int,
            salary: float,
            job: str
    ) -> None:
        employee = Employee(name, id, age, salary, job)
        self.employees.append(employee)

    def add_client(
            self,
            name: str,
            id : int,
            nsaucers: int,
            ndrinks: int,
            table: int
    ) -> None:
        client = Client(name, id)
        client.create_order(nsaucers,ndrinks,False,table)
        self.clients.append(client)
    
    