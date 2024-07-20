import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
from connection import *  


class Main:
    def __init__(self,data):
        self.data=data
        print(data)
        self.root = tk.Tk()
        self.root.geometry('700x600')
        self.root.title('Insert Form')

        self.conn = Connect()  
        self.cr = self.conn.cursor() 

        self.title = tk.Label(self.root, text='view Admin', font=("Arial", '20', 'bold'))
        self.title.pack(pady=20)

        self.formFont = ("Arial", 14)

        self.formFrame = tk.Frame(self.root)
        self.formFrame.pack()

        self.lb1 = tk.Label(self.formFrame, text='ID', font=self.formFont)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tk.Entry(self.formFrame, font=self.formFont)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        
        self.txt1.insert(0,self.data[0])
        self.txt1.configure(state="readonly")
        
       

        self.lb2 = tk.Label(self.formFrame, text='Enter Name', font=self.formFont)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tk.Entry(self.formFrame, font=self.formFont)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0,self.data[1])
        

        self.lb3 = tk.Label(self.formFrame, text='Enter Email', font=self.formFont)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tk.Entry(self.formFrame, font=self.formFont)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0,self.data[2])

        self.lb4 = tk.Label(self.formFrame, text='Enter Mobile', font=self.formFont)
        self.lb4.grid(row=3 , column=0, padx=10, pady=10)
        self.txt4 = tk.Entry(self.formFrame,font=self.formFont) 
        self.txt4.grid(row=3 , column=1, padx=10, pady=10)
        self.txt4.insert(0,self.data[3])
        
        self.lb5 = tk.Label(self.formFrame, text='Select Role', font=self.formFont)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = ttk.Combobox(self.formFrame, values=["Super Admin", "Admin"], font=self.formFont, state='readonly')
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.insert(0,self.data[4])
        

        self.btn = tk.Button(self.root, text="Submit", font=self.formFont, command=self.getFormValues)
        self.btn.pack(pady=10)

        self.btnFrame = tk.Frame(self.root)
        self.btnFrame.pack(pady=10)

        self.updateBtn = tk.Button(self.btnFrame, text="Update", font=self.formFont, command=self.getFormValues)
        self.updateBtn.grid(row=0, column=1, padx=10,pady=10)
        
        self.root.mainloop()
    

    def getFormValues(self):
        self.id = self.txt1.get()
        self.name = self.txt2.get()
        self.email = self.txt3.get()
        self.mobile = self.txt4.get()
        self.role = self.txt5.get()

        

        if self.id == '' or self.name == "" or self.email == '' or self.mobile == "" or self.role == "":
            msg.showwarning("Warning", "Please Enter Values.")

        else:
            if email_valid(self.email):
                if mobile_valid(self.mobile):
                 q =f"select * from view_admin where email='{self.email}'"
                 self.cr.execute(q)
                 email=self.cr.fetchall()
                 if len(email)==0:
                     q=f"select * from view_admin where mobile='{self.mobile}'"
                     self.cr.execute(q)
                     mobile=self.cr.fetchall()
                     if len(mobile)==0:
                         if email_valid(self.email):
                             if mobile_valid(self.mobile):
                                 q= f"insert into view_admin (name, email, mobile, password, role)values('{self.name}', '{self.email}', '{self.mobile}', '{self.password}', '{self.role}')"
                                 try:
                                     self.cr.execute(q)
                                     self.conn.commit()
                                     msg.showinfo('Success', 'Record inserted successfully!')

                                 except Exception as e:
                                     
                                     msg.showerror('Error', f'Error inserting record: {str(e)}')
                                     
                else:
                    msg.showwarning("warning","enter correct mobile")
            else:
                 msg.showwarning("warning","enter correct email")        
            
    
    
#obj = Main()