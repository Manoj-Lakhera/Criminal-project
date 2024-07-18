from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('Python MySQL Read Operation')

        self.conn = Connect()
        self.cr = self.conn.cursor()


        self.mainLabel = Label(self.root, text='View admins',font=('Arial',28,'bold'))
        self.mainLabel.pack(pady=20)

        self.searchFrame = Frame(self.root)
        self.searchFrame.pack(pady=20)

        self.lbl = Label(self.searchFrame, text='Search admins', font=('Arial', 14))
        self.lbl.grid(row=0, column=0, pady=10, padx=10)
        self.txt1 = Entry(self.searchFrame, font=('Arial', 14))
        self.txt1.grid(row=0, column=1, pady=10, padx=10)
        self.btn1 = Button(self.searchFrame, text='Search', font=('Arial', 14), command=self.searchadmin)
        self.btn1.grid(row=0, column=2, pady=10, padx=10)
        self.btn2 = Button(self.searchFrame, text='Refresh', font=('Arial', 14), command=self.refreshTable)
        self.btn2.grid(row=0, column=3, pady=10, padx=10)



        self.adminTable = ttk.Treeview(self.root, columns=['id','name', 'email','mobile','role'])
        self.adminTable.pack(expand=True, fill='both', padx=20, pady=20)
        
        self.adminTable.heading('name', text="Name")
        
        self.adminTable.heading('email', text="Email")
        self.adminTable.heading('mobile', text="Mobile")
        self.adminTable.heading('role', text="Role")
        self.adminTable['show'] = 'headings'
        self.getValues()

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 14), rowheight=40)
        style.configure("Treeview.Heading", font=("Arial", 14))

        self.root.mainloop()

    def getValues(self):
        q = f"select * from admin"
        self.cr.execute(q)
        result = self.cr.fetchall()
        for row in self.adminTable.get_children():
            self.adminTable.delete(row)

        index = 0
        for row in result:
            self.adminTable.insert("", index=index, values=row)
            index += 1

    def refreshTable(self):
        self.txt1.delete(0, 'end')
        self.getValues()

    def searchadmin(self):
        text = self.txt1.get()
        q = f"select * from admin where name like '%{text}%' or email like '%{text}%' or mobile like '%{text}%' or role like '%{text}%'"
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.adminTable.get_children():
            self.adminTable.delete(row)

        index = 0
        for row in result:
            self.adminTable.insert("", index=index, values=row)
            index += 1


obj =Main()