from tkinter import *
from Person import Person
import Order

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

    def crear_ventana(self): 
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

        label_client = Label(text="Client")
        label_client.place(x=20, y=20)

        label_create_order = Label(text="create_order")
        label_create_order.place(x=20, y=50)

        label_nsaucers = Label(text="nsaucers")
        label_nsaucers.place(x=20, y=80)
        input_nsaucers = Entry()
        input_nsaucers.place(x=140, y=80, width=60)

        label_ndrinks = Label(text="ndrinks")
        label_ndrinks.place(x=20, y=110)
        input_ndrinks = Entry()
        input_ndrinks.place(x=140, y=110, width=60)

        label_order_status = Label(text="order_status")
        label_order_status.place(x=20, y=140)
        input_order_status = Entry()
        input_order_status.place(x=140, y=140, width=60)

        label_table = Label(text="table")
        label_table.place(x=20, y=170)
        input_table = Entry()
        input_table.place(x=140, y=170, width=60)

        btn_create_order = Button(text="create_order")
        btn_create_order.place(x=20, y=200)

        app.mainloop() 
