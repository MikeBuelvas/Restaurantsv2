from typing import Optional
from tkinter import *
import Saucer, Inventary


class Kitchen():
    def __init__(
            self,
            inventary: Inventary,
            saucers: Optional[list] = None
            
    ) -> None:
        self.inventary = inventary
        self.saucers = saucers

    def create_saucer(
            self,
            name: str,
            ingredients: list,
            description: str,
            price: float        
    ) -> None:
        saucer = Saucer(name,ingredients,description,price)
        self.Saucers.append(saucer)

    def cook_saucer(self, saucer: Saucer) -> None:
        for ingredient in saucer.ingredients:
            for x in range(len(self.inventary.ingredients)):
                if self.inventary.ingredients[x] == ingredient:
                    if self.inventary.ingredients[x][1] > 0:
                        self.inventary.ingredients[x][1]-=1
                    else:
                        pass
                
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

    label_kitchen = Label(text="Kitchen")
    label_kitchen.place(x=20, y=20)
    label_gen_invoice = Label(text="gen_invoice")
    label_gen_invoice.place(x=20, y=50)

    label_id = Label(text="id")
    label_id.place(x=20, y=80)
    input_id = Entry()
    input_id.place(x=140, y=80, width=60)


    label_client = Label(text="client")
    label_client.place(x=20, y=110)
    input_client = Entry()
    input_client.place(x=140, y=110, width=60)

    label_invoice = Label(text="invoice")
    label_invoice.place(x=20, y=140)
    input_invoice = Entry()
    input_invoice.place(x=140, y=140, width=60)

    btn_gen_invoice = Button(text="gen_invoice")
    btn_gen_invoice.place(x=20, y=170)
    
    app.mainloop()    