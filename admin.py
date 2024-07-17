import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
from connection import Connect

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('700x600')
        self.root.title('Insert Form')

        self.title = tk.Label(self.root, text='Add new Admin', font=("Arial", '20', 'bold'))
        self.title.pack(pady=20)

        self.formFont = ("Arial", 14)

        self.formFrame = tk.PanedWindow(self.root)
        self.formFrame.pack()

        self.lb1 = tk.Label(self.formFrame, text='Enter ID', font=self.formFont)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tk.Entry(self.formFrame, font=self.formFont)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = tk.Label(self.formFrame, text='Enter name', font=self.formFont)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tk.Entry(self.formFrame, font=self.formFont)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tk.Label(self.formFrame, text='Enter email', font=self.formFont)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tk.Entry(self.formFrame, font=self.formFont)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tk.Label(self.formFrame, text='Enter mobile', font=self.formFont)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tk.Entry(self.formFrame, font=self.formFont)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = tk.Label(self.formFrame, text='Enter password', font=self.formFont)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = tk.Entry(self.formFrame, font=self.formFont, show="*")
        self.txt5.grid(row=4, column=1, padx=10, pady=10)

        self.lb6 = tk.Label(self.formFrame, text='Enter role', font=self.formFont)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)

        role_values = ["Admin", "Super Admin"]
        self.role_combobox = ttk.Combobox(self.formFrame, values=role_values, font=self.formFont)
        self.role_combobox.grid(row=5, column=1, padx=10, pady=10)
        self.role_combobox.set("Select role")

        self.btnFrame = tk.Frame(self.root)
        self.btnFrame.pack(pady=10)

        self.searchBtn = tk.Button(self.btnFrame, text="Search", font=self.formFont, command=self.searchadmin)
        self.searchBtn.grid(row=0, column=0, padx=10, pady=10)
        self.submitBtn = tk.Button(self.btnFrame, text="Submit", font=self.formFont, command=self.getFormValues)
        self.submitBtn.grid(row=0, column=1, padx=10, pady=10)
        self.updateBtn = tk.Button(self.btnFrame, text="Update", font=self.formFont, command=self.updateadmin)
        self.updateBtn.grid(row=0, column=2, padx=10, pady=10)
        self.deleteBtn = tk.Button(self.btnFrame, text="Delete", font=self.formFont, command=self.deleteadmin)
        self.deleteBtn.grid(row=0, column=3, padx=10, pady=10)
        self.resetBtn = tk.Button(self.btnFrame, text="Reset", font=self.formFont, command=self.resetForm)
        self.resetBtn.grid(row=0, column=4, padx=10, pady=10)

        self.root.mainloop()

    def deleteadmin(self):
        self.conn = Connect()
        self.cr = self.conn.cursor()
        id = self.txt1.get()
        q = f"delete from admin where id = '{id}'"
        self.cr.execute(q)
        self.conn.commit()
        self.conn.close()
        msg.showinfo("Success", "admin has been Deleted.")
        self.resetForm()

    def searchadmin(self):
        self.conn = Connect()
        self.cr = self.conn.cursor()
        id = self.txt1.get()
        q = f"select * from admin where id='{id}'"
        self.cr.execute(q)
        result = self.cr.fetchall()
        self.conn.close()
        if len(result) == 0:
            msg.showwarning("Warning", "Invalid id.")
        else:
            admin = result[0]
            self.txt2.delete(0, tk.END)
            self.txt3.delete(0, tk.END)
            self.txt4.delete(0, tk.END)
            self.txt5.delete(0, tk.END)
            self.role_combobox.set("Select role")
            
            self.txt2.insert(0, admin[1])
            self.txt3.insert(0, admin[2])
            self.txt4.insert(0, admin[3])
            self.txt5.insert(0, admin[4])
            self.role_combobox.set(admin[5])

    def resetForm(self):
        self.txt1.delete(0, tk.END)
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')
        self.txt4.delete(0, 'end')
        self.txt5.delete(0, 'end')
        self.role_combobox.set("Select role")

    def getFormValues(self):
        self.id = self.txt1.get()
        self.name = self.txt2.get()
        self.email = self.txt3.get()
        self.mobile = self.txt4.get()
        self.password = self.txt5.get()
        self.role = self.role_combobox.get()

        if self.id == '' or self.name == '' or self.email == "" or self.mobile == '' or self.password == "" or self.role == 'Select role':
            msg.showwarning("Warning", "Please Enter Values.")
        else:
            self.conn = Connect()
            self.cr = self.conn.cursor()
            q = f"insert into admin (id, name, email, mobile, password, role) values ('{self.id}', '{self.name}', '{self.email}', '{self.mobile}', '{self.password}', '{self.role}')"
            self.cr.execute(q)
            self.conn.commit()
            self.conn.close()
            msg.showinfo('Success', 'data has been Added')
            self.resetForm()

    def updateadmin(self):
        self.id = self.txt1.get()
        self.name = self.txt2.get()
        self.email = self.txt3.get()
       
        self.mobile = self.txt4.get()
        self.password = self.txt5.get()
        self.role = self.role_combobox.get()

        if self.id == '' or self.name == '' or self.email == "" or self.mobile == '' or self.password == "" or self.role == 'Select role':
            msg.showwarning("Warning", "Please Enter Values.")
        else:
            self.conn = Connect()
            self.cr = self.conn.cursor()
            q = f"update admin set name='{self.name}', email='{self.email}', mobile='{self.mobile}', password='{self.password}', role='{self.role}' where id='{self.id}'"
            self.cr.execute(q)
            self.conn.commit()
            self.conn.close()
            msg.showinfo('Success', 'data has been Updated')
            self.resetForm()

obj = Main()
