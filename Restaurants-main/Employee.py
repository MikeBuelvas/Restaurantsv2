import Person

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


