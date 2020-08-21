from tkinter import *

# -------------------------- Root -----------------------------------------------------------------------------------------------------------------------------------------------------------------
class Product:
    global IMG

    def __init__(self,root):
        self.root = root
        self.root.title("PRODUCTOS DANIEL JOYAS")
        root.iconbitmap("img\logo.ico")
        
# -------------------------- Frame -----------------------------------------------------------------------------------------------------------------------------------------------------------------

        my_frame = Frame()
        my_frame.pack()

        buttons_frame = Frame()
        buttons_frame.pack()


# -------------------------- Title + Logo ------------------------------------------------------------------------------------------------------------------------------------------------------------

        lbl_logo = Label(my_frame,image = IMG).grid(row=0,column=1,padx=10,pady=4,columnspan=5)

# -------------------------- Labels -----------------------------------------------------------------------------------------------------------------------------------------------------------------
        lbl_id = Label(my_frame,text="ID: ",font=("Calibri",14))
        lbl_id.grid(row=2,column=1,padx=10,pady=4,sticky="w")

        lbl_name = Label(my_frame,text="NAME: ",font=("Calibri",14))
        lbl_name.grid(row=3,column=1,padx=10,pady=4,sticky="w")

        lbl_price = Label(my_frame,text="PRICE: ",font=("Calibri",14))
        lbl_price.grid(row=4,column=1,padx=10,pady=4,sticky="w")

        lbl_material = Label(my_frame,text="MATERIAL: ",font=("Calibri",14))
        lbl_material.grid(row=5,column=1,padx=10,pady=4,sticky="w")

        lbl_large = Label(my_frame,text="LARGE: ",font=("Calibri",14))
        lbl_large.grid(row=6,column=1,padx=10,pady=4,sticky="w")

        lbl_size = Label(my_frame,text="SIZE: ",font=("Calibri",14))
        lbl_size.grid(row=7,column=1,padx=10,pady=4,sticky="w")

        lbl_stock = Label(my_frame,text="STOCK: ",font=("Calibri",14))
        lbl_stock.grid(row=8,column=1,padx=10,pady=4,sticky="w")
# -------------------------- Entrys -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        entry_id = Entry(my_frame).grid(row=2,column=2,pady=4,sticky="w")

        entry_name = Entry(my_frame).grid(row=3,column=2,pady=4,sticky="w")

        entry_price = Entry(my_frame).grid(row=4,column=2,pady=4,sticky="w")

        entry_material = Entry(my_frame).grid(row=5,column=2,pady=4,sticky="w")

        entry_large = Entry(my_frame).grid(row=6,column=2,pady=4,sticky="w")

        entry_size = Entry(my_frame).grid(row=7,column=2,pady=4,sticky="w")

        entry_stock = Entry(my_frame).grid(row=8,column=2,pady=4,sticky="w")
# -------------------------- Buttons -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        create_button = Button(buttons_frame,text="CREATE").grid(row=1,column=1,padx=10,pady=4)
        read_button = Button(buttons_frame,text="READ").grid(row=1,column=2,padx=10,pady=4)
        update_button = Button(buttons_frame,text="UPDATE").grid(row=1,column=3,padx=10,pady=4)
        delete_button = Button(buttons_frame,text="DELETE").grid(row=1,column=4,padx=10,pady=4)
        list_button = Button(buttons_frame,text="LIST").grid(row=1,column=5,padx=10,pady=4)
# -------------------------- TextBox -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        text_box = Text(my_frame,width=32,height=15).grid(row=2,column=3,padx=10,pady=4,columnspan=3,rowspan=7)


# -------------------------- EnterPoint -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk()
    IMG = PhotoImage(file="img\logo1.png")
    aplication = Product(root)
    root.mainloop()