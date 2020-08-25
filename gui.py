from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import pymysql
import password
# -------------------------- Root -----------------------------------------------------------------------------------------------------------------------------------------------------------------
class Product:
    global IMG

    def __init__(self,root):
        self.root = root
        self.widgets()

    def widgets(self):
# -------------------------- Menu ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        menubar = Menu(root)
        
        bbdd_menu = Menu(menubar,tearoff=0)
        bbdd_menu.add_command(label="Connect",command=self.connect)
        bbdd_menu.add_separator()
        bbdd_menu.add_command(label="Exit",command=self.exit_app)

        help_menu = Menu(menubar,tearoff=0)
        help_menu.add_command(label="User guide",command=self.show_help)
        help_menu.add_command(label="About..")
        
        menubar.add_cascade(label="BBDD",menu=bbdd_menu)
        menubar.add_cascade(label="Help",menu=help_menu)

        root.config(menu=menubar)
        
# -------------------------- Frame -----------------------------------------------------------------------------------------------------------------------------------------------------------------

        my_frame = Frame()
        my_frame.pack()

        buttons_frame = Frame()
        buttons_frame.pack()


# -------------------------- Logo ------------------------------------------------------------------------------------------------------------------------------------------------------------

        lbl_logo = Label(my_frame,image = IMG).grid(row=0,column=0,padx=10,pady=4,columnspan=3)

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

        # lbl_info = Label(my_frame,text = """------------------------------------------------------------------------------------------------------------------------------""")
        # lbl_info.grid(row=9,column=3,padx=10,pady=4,columnspan=7,rowspan=2)

# -------------------------- Entrys -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.uid = StringVar()
        self.name = StringVar()
        self.price = StringVar()
        self.material = StringVar()
        self.large = StringVar()
        self.size = StringVar()
        self.stock = StringVar()
        
        entry_id = Entry(my_frame, textvariable=self.uid ).grid(row=2,column=2,pady=4,sticky="w")

        entry_name = Entry(my_frame, textvariable=self.name).grid(row=3,column=2,pady=4,sticky="w")

        entry_price = Entry(my_frame, textvariable=self.price).grid(row=4,column=2,pady=4,sticky="w")

        entry_material = Entry(my_frame, textvariable=self.material).grid(row=5,column=2,pady=4,sticky="w")

        entry_large = Entry(my_frame, textvariable=self.large).grid(row=6,column=2,pady=4,sticky="w")

        entry_size = Entry(my_frame, textvariable=self.size).grid(row=7,column=2,pady=4,sticky="w")

        entry_stock = Entry(my_frame, textvariable=self.stock).grid(row=8,column=2,pady=4,sticky="w")
# -------------------------- Buttons -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        create_button = Button(buttons_frame,text="CREATE").grid(row=1,column=1,padx=10,pady=4)

        search_button = Button(buttons_frame,text="SEARCH").grid(row=1,column=2,padx=10,pady=4)

        update_button = Button(buttons_frame,text="UPDATE").grid(row=1,column=3,padx=10,pady=4)

        delete_button = Button(buttons_frame,text="DELETE").grid(row=1,column=4,padx=10,pady=4)

        list_button = Button(buttons_frame,text="LIST", command= self.list_products).grid(row=1,column=5,padx=10,pady=4)

        clear_button = Button(buttons_frame,text="CLEAR", command = self.clear_gui).grid(row=1,column=6,padx=10,pady=4)
# -------------------------- Table -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.table = ttk.Treeview(my_frame,height =11)
        self.table.grid(row=2,column=3,padx=10,pady=4,rowspan=7,columnspan=7)
        
        # columns
        self.table["columns"] = ("NAME","PRICE","MATERIAL","LARGE","SIZE","STOCK")
        self.table.column("#0",width=50,minwidth=50)
        self.table.column("#1",width=250,minwidth=50)
        self.table.column("#2",width=100,minwidth=50)
        self.table.column("#3",width=100,minwidth=50)
        self.table.column("#4",width=50,minwidth=50)
        self.table.column("#5",width=50,minwidth=50)
        self.table.column("#6",width=50,minwidth=50)
        # headings
        self.table.heading("#0", text="ID",anchor=CENTER)
        self.table.heading("#1", text="NAME",anchor=CENTER)
        self.table.heading("#2", text="PRICE",anchor=CENTER)
        self.table.heading("#3", text="MATERIAL",anchor=CENTER)
        self.table.heading("#4", text="LARGE",anchor=CENTER)
        self.table.heading("#5", text="SIZE",anchor=CENTER)
        self.table.heading("#6", text="STOCK",anchor=CENTER)



#---------------------------Functions -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def connect(self):
        self.connection = pymysql.connect(
                host="localhost",
                user="root",
                password=password.contra,
                db="daniel-joyas"
                )

        self.cursor = self.connection.cursor()    

        query = """ SET character_set_client = utf8mb4 ;
        CREATE TABLE IF NOT EXISTS`products` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(45) NOT NULL,
        `material` varchar(45) DEFAULT NULL,
        `price` int(11) NOT NULL,
        `large` varchar(45) DEFAULT NULL,
        `size` varchar(45) DEFAULT NULL,
        `stock` varchar(45) NOT NULL DEFAULT '0',
        PRIMARY KEY (`id`)
        ) ENGINE=MyISAM DEFAULT CHARSET=utf8;"""
        try:
                self.cursor.execute(query)
                messagebox.showinfo("Connected","BBDD created. Connection established.") 
        except:
                messagebox.showinfo("Connection","BBDD already exists, connection established.")
    
    def _run_query(self, query, parameters = ()):
        self.connection = pymysql.connect(
                host="localhost",
                user="root",
                password=password.contra,
                db="daniel-joyas"
                )

        cursor = self.connection.cursor()
        result = cursor.execute(query, parameters)

        self.connection.commit()
        self.connection.close()
        return result

    def show_help(self):
        messagebox.showinfo("User guide","""
        Start conecting with the database by BBDD > Connect


        -CREATE: fill all the fields (only material, large and size can be null) then click on CREATE.

        -SEARCH: fill the fields that you are looking for an click on SEARCH.

        -UPDATE: fill the ID field, click on UPDATE, fill with the new fields and accept.

        -DELETE: fill the ID field, click on DELETE and accept.

        -LIST: click on LIST to show all the registers.

        -CLEAR: click on CLEAR to clear all the fields and the table.


        BBDD > Exit to close the aplication.
        """)

    def exit_app(self):
            choice = messagebox.askquestion("Exit","Do you wish to close?")

            if choice == "yes":
                    root.destroy()

    def clear_gui(self):
        self.uid.set("")
        self.name.set("")
        self.price.set("")
        self.material.set("")
        self.large.set("")
        self.size.set("")
        self.stock.set("")

        records = self.table.get_children()
        for element in records:
                self.table.delete(element)
        
        
        
    def create_product(self):
        pass
    def search_product(self):
        pass
    def update_product(self):
        pass
    def delete_product(self):
        pass


    def list_products(self):
        self.clear_gui()
        query = "SELECT * FROM `daniel-joyas`.products ORDER BY name DESC;"
        db_rows = self._run_query(query)
        for row in db_rows:
                print(row)


# -------------------------- EnterPoint -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    root = Tk()
    root.title("PRODUCTOS DANIEL JOYAS")
    root.iconbitmap("img\logo.ico")
    IMG = PhotoImage(file="img\logo1.png")
    aplication = Product(root)
    root.mainloop()