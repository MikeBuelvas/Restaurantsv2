import pickle
from tkinter import *
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
        self.admin = Employee("Mike Buelvas", 123456789,20,2555.4,"Administrador")

        #self.cash_register
        archive_balance = open("archive_balance","ab+")
        archive_sales = open("archive_sales","ab+")
        archive_balance.seek(0)
        archive_sales.seek(0)
        try:
            balance = pickle.load(archive_balance)
            sales = pickle.load(archive_sales)
            self.cash_register = Cash_Register(balance, self.admin, self.admin.id, sales)
        except:
            sales = []
            self.cash_register = Cash_Register(0, self.admin, self.admin.id, sales)
        finally:
            archive_balance.close()
            archive_sales.close()
            del(archive_balance)
            del(archive_sales)

        #self.employees
        archive_employees = open("archive_employees","ab+")
        archive_employees.seek(0)
        try:
            self.employees = pickle.load(archive_employees)        
        except:
            self.employees = []
        finally:
            archive_employees.close()
            del(archive_employees)
        
        #self.clients
        archive_clients = open("archive_clients","ab+")
        archive_clients.seek(0)
        try:
            self.clients = pickle.load(archive_clients)        
        except:
            self.clients = []
        finally:
            archive_clients.close()
            del(archive_clients)

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
        self.save_e()

    def add_client(
            self,
            name: str,
            id: int
    ) -> None:
        client = Client(name,id)
        self.clients.append(client)
        self.save_c()


    def save_e(self) -> None:
            archive_employees = open("archive_employees","wb")
            pickle.dump(self.employees, archive_employees)
            archive_employees.close()
            del(archive_employees)
            
    def save_c(self) -> None:
            archive_clients = open("archive_clients","wb")
            pickle.dump(self.clients, archive_clients)
            archive_clients.close()
            del(archive_clients)

