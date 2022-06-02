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

    app=Tk()
    app.title("Restaurant")
    app.iconbitmap('./imgs/logo.ico')
    app.geometry("612x410")
    app.resizable(False, False)

    main_img = PhotoImage(file = "./imgs/fondo.gif")


    frame = Frame(app, width=612, height=410)
    frame.pack()


    label = Label(frame, image = main_img)
    label.pack()
    i = int(input("1. Digite 1 si desea agregar cliente.\n"+
    "2. Digite 2 si desea agregar cliente\n = "))
    if i==1:
        label_Restaurant = Label(text="Restaurant")
        label_Restaurant.place(x=20, y=20)
        label_add_client = Label(text="add_client")
        label_add_client.place(x=20, y=50)

        label_name = Label(text="name")
        label_name.place(x=20, y=80)
        input_name = Entry()
        input_name.place(x=140, y=80, width=60)

        label_id = Label(text="id")
        label_id.place(x=20, y=110)
        input_id = Entry()
        input_id.place(x=140, y=110, width=60)

        label_nsaucers = Label(text="nsaucers")
        label_nsaucers.place(x=20, y=140)
        input_nsaucers = Entry()
        input_nsaucers.place(x=140, y=140, width=60)

        label_ndrinks = Label(text="ndrinks")
        label_ndrinks.place(x=20, y=170)
        input_ndrinks = Entry()
        input_ndrinks.place(x=140, y=170, width=60)

        label_table = Label(text="table")
        label_table.place(x=20, y=200)
        input_table = Entry()
        input_table.place(x=140, y=200, width=60)

        btn_add_client = Button(text="add_client")
        btn_add_client.place(x=20, y=230)

    if i == 2:
        label_Restaurant = Label(text="Restaurant")
        label_Restaurant.place(x=20, y=20)
        label_add_employee = Label(text="add_employee")
        label_add_employee.place(x=20, y=50)

        label_name = Label(text="name")
        label_name.place(x=20, y=80)
        input_name = Entry()
        input_name.place(x=140, y=80, width=60)

        label_id = Label(text="id")
        label_id.place(x=20, y=110)
        input_id = Entry()
        input_id.place(x=140, y=110, width=60)

        label_age = Label(text="age")
        label_age.place(x=20, y=140)
        input_age = Entry()
        input_age.place(x=140, y=140, width=60)

        label_salary = Label(text="salary")
        label_salary.place(x=20, y=170)
        input_salary = Entry()
        input_salary.place(x=140, y=170, width=60)

        label_job = Label(text="job")
        label_job.place(x=20, y=210)
        input_job = Entry()
        input_job.place(x=140, y=210, width=60)

        btn_add_employee = Button(text="add_employee")
        btn_add_employee.place(x=20, y=240)

    app.mainloop() 