import tkinter
from tkinter import messagebox as msg
from connection import *
from tkinter import ttk


class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("650x650")
        self.root.title("Insert Form")
        self.title = tkinter.Label(self.root, text="Add Admin", font=("Arial", "20", "bold"))
        self.title.pack(pady=10)

        self.formFont = ("Arial", 14)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.formFrame = tkinter.PanedWindow(self.root)
        self.formFrame.pack()

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Name", font=self.formFont)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.formFrame, font=self.formFont)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.btn1=tkinter.Button(self.formFrame,text="Search",command=self.searchAdmin,font=self.formFont)
        self.btn1.grid(row=0, column=2, padx=10, pady=10)
        self.btn2 = tkinter.Button(self.formFrame, text="Reset", command=self.resetAdmin, font=self.formFont)
        self.btn2.grid(row=0, column=3, padx=10, pady=10)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Email", font=self.formFont)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.formFont)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tkinter.Label(self.formFrame, text="Enter Mobile", font=self.formFont)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.formFrame, font=self.formFont)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tkinter.Label(self.formFrame, text="Enter Password", font=self.formFont)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tkinter.Entry(self.formFrame, font=self.formFont, show="*")
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = tkinter.Label(self.formFrame, text="Enter Role", font=self.formFont)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)

        # Define role values
        role_values = ["Admin", "Super Admin"]

        # Create the combobox
        self.role_combobox = ttk.Combobox(self.formFrame, values=role_values, font=self.formFont)
        self.role_combobox.grid(row=4, column=1, padx=10, pady=10)

        self.buttonFrame=tkinter.Frame(self.root)
        self.buttonFrame.pack()

        self.btn3=tkinter.Button(self.buttonFrame,text="Update",font=self.formFont,command=self.getFormValues)
        self.btn3.grid(row=0, column=0, padx=10, pady=10)

        self.btn4 = tkinter.Button(self.buttonFrame, text="Delete", font=self.formFont, command=self.deleteAdmin)
        self.btn4.grid(row=0, column=1, padx=10, pady=10)

        # self.btn = tkinter.Button(self.root, text="Submit", font=self.formFont, command=self.getFormValues)
        # self.btn.pack(pady=10)

        self.root.mainloop()

    def getFormValues(self):
        self.name=self.txt1.get()
        self.email=self.txt2.get()
        self.mobile=self.txt3.get()
        self.password = self.txt4.get()
        self.role = self.role_combobox.get()

        if self.name == "" or self.email == "" or self.mobile == "" or self.password == "" or self.role=='':
            msg.showwarning("Warning", "Enter your Values")
        else:
            q4=f"select * from admin where email='{self.email}'"
            self.cur.execute(q4)
            email=self.cur.fetchall()
            if len(email)==0:
                q5=f"select * from admin where mobile='{self.mobile}'"
                self.cur.execute(q5)
                mobile=self.cur.fetchall()
                if len(mobile)==0:
                    if email_valid(self.email):
                        if mobile_valid(self.mobile):
                            q=f"insert into admin values(null,'{self.name}', '{self.email}', '{self.mobile}','{self.password}','{self.role}')"
                            self.cur.execute(q)
                            self.conn.commit()
                            msg.showwarning("Success", "Admin has been added")
                        else:
                            msg.showwarning("Warning","Enter valid mobile no")

                    else:
                        msg.showwarning("Warning","enter valid email address")
                else:
                    msg.showwarning("Warning","mobile already exist")
            else:
                msg.showwarning("Warning","Email already exist")
    def searchAdmin(self):
        self.name=self.txt1.get()
        q1=f"select * from admin where name='{self.name}'"
        self.cur.execute(q1)
        self.conn.commit()
        res=self.cur.fetchall()
        if len(res)==0:
            msg.showwarning("Warning", "Enter correct name.")
        else:
            admin=res[0]
            self.txt2.insert(0,admin[2])
            self.txt3.insert(0,admin[3])
            self.txt4.insert(0,admin[4])
            self.role_combobox.insert(0,admin[5])

    def resetAdmin(self):
        self.txt1.delete(0,"end")
        self.txt2.delete(0, "end")
        self.txt3.delete(0, "end")
        self.txt4.delete(0, "end")
        self.role_combobox.delete(0,"end")

    def deleteAdmin(self):
        self.name=self.txt1.get()
        q2=f"delete from admin where name='{self.name}'"
        self.cur.execute(q2)
        self.conn.commit()
        msg.showwarning("Warning", "Admin deleted successfully")
        self.resetAdmin()


obj=Main()