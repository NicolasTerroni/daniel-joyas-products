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
        """Window widgets"""
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

        # Output label
        self.lbl_output = Label(my_frame,text = "Disconnected",fg = "#969696")
        self.lbl_output.grid(row=1,column=3,padx=10,pady=4,columnspan=7,sticky=W + E)

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
        create_button = Button(buttons_frame,text="CREATE", command=self.create_product)
        create_button.grid(row=1,column=1,padx=10,pady=4)

        search_button = Button(buttons_frame,text="SEARCH", command = self.search_product)
        search_button.grid(row=1,column=2,padx=10,pady=4)

        update_button = Button(buttons_frame,text="UPDATE", command = self.update_product_window)
        update_button.grid(row=1,column=3,padx=10,pady=4)

        delete_button = Button(buttons_frame,text="DELETE", command = self.delete_product)
        delete_button.grid(row=1,column=4,padx=10,pady=4)

        list_button = Button(buttons_frame,text="LIST ALL", command= self.list_products)
        list_button.grid(row=1,column=5,padx=10,pady=4)

        clear_button = Button(buttons_frame,text="CLEAR ALL", command = self.clear_gui)
        clear_button.grid(row=1,column=6,padx=10,pady=4)
        
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
        self.table.heading("#2", text="MATERIAL",anchor=CENTER)
        self.table.heading("#3", text="PRICE",anchor=CENTER)
        self.table.heading("#4", text="LARGE",anchor=CENTER)
        self.table.heading("#5", text="SIZE",anchor=CENTER)
        self.table.heading("#6", text="STOCK",anchor=CENTER)


#---------------------------Functions -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def connect(self):
        """Connects to the database (or creates it if not exists)"""
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
        finally:
            self.lbl_output["text"] = "Connection established."
            self.list_products()


    def _run_query(self, query):
        """Tries to run a query"""
        try:
            result = self.cursor.execute(query)
        except:
            messagebox.showerror("Error","""
Something went wrong executing the query.

Check if you are connected to the database.

If you are trying to manipulate data, check if you filled in the fields correctly.

If you were using delete or update you must select a register on the table before.'""")

        self.connection.commit()
        return result


    def show_help(self):
        """Shows the help window"""
        messagebox.showinfo("User guide","""
        Start conecting with the database by BBDD > Connect


        -CREATE: fill all the fields (only material, large and size can be null) then click on CREATE.

        -SEARCH: fill the ID field that you are looking for an click on SEARCH.

        -UPDATE: Select a record on the table and click on UPDATE, then fill in the new fields and confirm.

        -DELETE: Select a record on the table and click on DELETE.

        -LIST ALL: click on LIST ALL to show all the registers.

        -CLEAR ALL: click on CLEAR ALL to clear all the fields and the table.


        BBDD > Exit to close the aplication.
        """)


    def exit_app(self):
        """Closes the app"""
        choice = messagebox.askquestion("Exit","Do you wish to close?")

        if choice == "yes":
            self.connection.close()
            root.destroy()


    def _clear_table(self):
        """Clears the table's content"""
        records = self.table.get_children()
        for element in records:
                self.table.delete(element)


    def clear_gui(self):
        """Clears all the entrys and the table"""
        self.uid.set("")
        self.name.set("")
        self.price.set("")
        self.material.set("")
        self.large.set("")
        self.size.set("")
        self.stock.set("")
        self._clear_table()
        

    def _validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0


    def create_product(self):
        """Gets data, creates a product"""
        input_name = self.name.get()
        input_price = self.price.get()
        input_material = self.material.get()
        input_large = self.large.get()
        input_size = self.size.get()
        input_stock = self.stock.get()

        query = f"INSERT INTO products(name,material,price,large,size,stock) VALUES('{input_name}','{input_material}',{input_price},'{input_large}','{input_size}',{input_stock});"     
        
        if self._validation():
            self._run_query(query)
            self.lbl_output["text"] = f"Product '{input_name}' created successfully."
            self.list_products()
        else:
            self.lbl_output["text"] = f"Product creation failed. Check if you entered the fields correctly"


    def search_product(self):
        """Gets id, shows a product"""
        input_uid = self.uid.get()
        query = f"SELECT * FROM products WHERE id={input_uid};"

        try:
            self._run_query(query)
            db_row = self.cursor.fetchone()
            self.clear_gui()
            self.table.insert("",0, text = db_row[0], values = (db_row[1],db_row[2],db_row[3],db_row[4],db_row[5],db_row[6]))
        except:
            messagebox.showinfo("Search","Product ID doesn't exist.")


    def update_product_window(self):
        """Open the update window"""
        selected_product = self.table.item(self.table.selection())

        try:
            #Get selected values
            selected_product_id = selected_product["text"]
            old_name = selected_product["values"][0]
            old_material = selected_product["values"][1]
            old_price = selected_product["values"][2]
            old_large = selected_product["values"][3]
            old_size = selected_product["values"][4]
            old_stock = selected_product["values"][5]
            
            #Window
            self.update_window = Toplevel()
            self.update_window.title("Update product")

            #Old product labels
            selected_product_id_lbl = Label(self.update_window, text= f"UPDATING PRODUCT ID: {selected_product_id}")
            selected_product_id_lbl.grid(row=1,column=1,padx=4,pady=4,sticky=W)

            old_name_lbl = Label(self.update_window, text= f"Old name: '{old_name}''",fg="#7F7F7F")
            old_name_lbl.grid(row=2,column=1,padx=4,pady=4,sticky=W)

            old_price_lbl = Label(self.update_window, text= f"Old price: {old_price}",fg="#7F7F7F")
            old_price_lbl.grid(row=3,column=1,padx=4,pady=4,sticky=W)

            old_material_lbl = Label(self.update_window, text= f"Old material: '{old_material}''",fg="#7F7F7F")
            old_material_lbl.grid(row=4,column=1,padx=4,pady=4,sticky=W)

            old_large_lbl = Label(self.update_window, text= f"Old large: '{old_large}''",fg="#7F7F7F")
            old_large_lbl.grid(row=5,column=1,padx=4,pady=4,sticky=W)

            old_size_lbl = Label(self.update_window, text= f"Old size: '{old_size}''",fg="#7F7F7F")
            old_size_lbl.grid(row=6,column=1,padx=4,pady=4,sticky=W)

            old_stock_lbl = Label(self.update_window, text= f"Old stock: {old_stock}",fg="#7F7F7F")
            old_stock_lbl.grid(row=7,column=1,padx=4,pady=4,sticky=W)

            # New product labels
            new_name_lbl = Label(self.update_window, text= "New name: ")
            new_name_lbl.grid(row=2,column=2,padx=4,pady=4,sticky=W)

            new_price_lbl = Label(self.update_window, text= "New price: ")
            new_price_lbl.grid(row=3,column=2,padx=4,pady=4,sticky=W)

            new_material_lbl = Label(self.update_window, text= "New material: ")
            new_material_lbl.grid(row=4,column=2,padx=4,pady=4,sticky=W)

            new_large_lbl = Label(self.update_window, text= "New large: ")
            new_large_lbl.grid(row=5,column=2,padx=4,pady=4,sticky=W)

            new_size_lbl = Label(self.update_window, text= "New size: ")
            new_size_lbl.grid(row=6,column=2,padx=4,pady=4,sticky=W)

            new_stock_lbl = Label(self.update_window, text= "New stock: ")
            new_stock_lbl.grid(row=7,column=2,padx=4,pady=4,sticky=W)

            # Entrys
            upd_name = StringVar()
            upd_price = StringVar()
            upd_material = StringVar()
            upd_large = StringVar()
            upd_size = StringVar()
            upd_stock = StringVar()

            new_name = Entry(self.update_window, textvariable= upd_name)
            new_name.grid(row=2,column=3,padx=4,pady=4,sticky=W)

            new_price = Entry(self.update_window, textvariable= upd_price)
            new_price.grid(row=3,column=3,padx=4,pady=4,sticky=W)

            new_material = Entry(self.update_window, textvariable= upd_material)
            new_material.grid(row=4,column=3,padx=4,pady=4,sticky=W)

            new_large = Entry(self.update_window, textvariable= upd_large)
            new_large.grid(row=5,column=3,padx=4,pady=4,sticky=W)

            new_size = Entry(self.update_window, textvariable= upd_size)
            new_size.grid(row=6,column=3,padx=4,pady=4,sticky=W)

            new_stock = Entry(self.update_window, textvariable= upd_stock)
            new_stock.grid(row=7,column=3,padx=4,pady=4,sticky=W)

            # Confirm button
            updt_button = Button(self.update_window, text="CONFIRM UPDATE",
             command = lambda: self.update_product(
                 upd_name.get(),
                 upd_price.get(),
                 upd_material.get(),
                 upd_large.get(),
                 upd_size.get(),
                 upd_stock.get(),
                 selected_product_id
                 ))
            updt_button.grid(row=8,column=2,padx=4,pady=4,columnspan=2)

        except IndexError:
            self.lbl_output["text"] = f"No record selected to update."


    def update_product(self, upd_name, upd_price, upd_material, upd_large, upd_size, upd_stock, selected_product_id):
        """Runs the update query"""

        query = f"""
        UPDATE products SET 
        name='{upd_name}', 
        price={upd_price}, 
        material='{upd_material}', 
        large='{upd_large}', 
        size='{upd_size}', 
        stock='{upd_stock}' 
        WHERE id={selected_product_id};"""
        
        question = messagebox.askquestion("Update",f"Are you sure you want to update the product id={selected_product_id} ?")
        if question == "yes":
            self._run_query(query)
            self.update_window.destroy()
            self.lbl_output["text"] = f"Product {selected_product_id} updated."
            self.list_products()


    def delete_product(self):
        """Deletes the selected record."""
        
        selected_product_id = self.table.item(self.table.selection())["text"]
        query = f"DELETE FROM products WHERE id={selected_product_id};"

        question = messagebox.askquestion("Delete",f"Are you sure you want to delete the product id={selected_product_id} ?")
        if question == "yes":
            try:
                self._run_query(query)
                self.lbl_output["text"] = f"Product {selected_product_id} deleted."

            except:
                self.lbl_output["text"] = f"No record selected to delete."
            
            finally:
                    self.list_products()


    def list_products(self):
        """Show all products on the table"""
        self.clear_gui()

        query = "SELECT * FROM products ORDER BY id DESC;"
        self._run_query(query)

        db_rows = self.cursor.fetchall()
        for row in db_rows:
            self.table.insert("",0, text = row[0], values = (row[1],row[2],row[3],row[4],row[5],row[6]))


# -------------------------- EnterPoint -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk()
    root.title("PRODUCTS - DANIEL JOYAS")
    root.iconbitmap("img\logo.ico")
    IMG = PhotoImage(file="img\logo1.png")
    aplication = Product(root)
    root.mainloop()