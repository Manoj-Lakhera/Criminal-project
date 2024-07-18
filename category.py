import tkinter
from tkinter import messagebox as msg
from connection import Connect
from tkinter import ttk


class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("600x600")
        self.root.title("Insert Form")
        self.title = tkinter.Label(self.root, text="Add Category", font=("Arial", "20", "bold"))
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
        self.btn1=tkinter.Button(self.formFrame,text="Search",command=self.searchCategory,font=self.formFont)
        self.btn1.grid(row=0, column=2, padx=10, pady=10)
        self.btn2 = tkinter.Button(self.formFrame, text="Reset", command=self.resetCategory, font=self.formFont)
        self.btn2.grid(row=0, column=3, padx=10, pady=10)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Description", font=self.formFont)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.formFont)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.buttonFrame=tkinter.Frame(self.root)
        self.buttonFrame.pack()

        self.btn3=tkinter.Button(self.buttonFrame,text="Update",font=self.formFont,command=self.getFormValues)
        self.btn3.grid(row=0, column=0, padx=10, pady=10)

        self.btn4 = tkinter.Button(self.buttonFrame, text="Delete", font=self.formFont, command=self.deleteCategory)
        self.btn4.grid(row=0, column=1, padx=10, pady=10)

        self.root.mainloop()

    def getFormValues(self):
        self.name=self.txt1.get()
        self.description=self.txt2.get()

        if self.name == "" or self.description == "" :
            msg.showwarning("Warning", "Enter your Values")
        else:
            q=f"insert into category values('{self.name}', '{self.description}')"
            self.cur.execute(q)
            self.conn.commit()
            msg.showwarning("Success", "Category added")

    def searchCategory(self):
        self.name=self.txt1.get()
        q1=f"select * from category where name='{self.name}'"
        self.cur.execute(q1)
        self.conn.commit()
        res=self.cur.fetchall()
        if len(res)==0:
            msg.showwarning("Warning", "Enter correct name.")
        else:
            admin=res[0]
            self.txt2.insert(0,admin[1])

    def resetCategory(self):
        self.txt1.delete(0,"end")
        self.txt2.delete(0, "end")

    def deleteCategory(self):
        self.name=self.txt1.get()
        q2=f"delete from category where name='{self.name}'"
        self.cur.execute(q2)
        self.conn.commit()
        msg.showwarning("Warning", "Category deleted successfully")
        self.resetCategory()


obj=Main()