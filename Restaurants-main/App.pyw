from tkinter import *

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

"""
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
"""

"""
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
"""

"""
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
"""

"""
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

"""

app.mainloop()