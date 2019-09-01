from tkinter import *
from tkinter import messagebox as tkmessagebox       # Opening Graphicbox
import pickle, os
import time
import tkinter as tk
import pandas
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score



# to read data from a csv file
#df = pandas.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\Blood Bank.csv")
#df.head()
#type(df)
#df.shape


class win1(Tk):    #Opening  tkinter window
    new = None


    def __init__(self, *arg):              #constructor  
        Tk.__init__(self, *arg)
        lab2 = Label(self, text='LifeLine', font=('Comic Sans MS', 70, 'bold'), fg='black', width=70 )
        lab2.pack()
        lab1 = Label(self, text='HACKKIDDIES', font=('Verdana', 30), fg='darkblue', width=81 )
        lab1.pack()
        lab1 = Label(self, text='Creators---                    ', font=('Times', 20, 'bold'), fg='gray', width=70 ,
                     justify='right')
        lab1.pack()
        
        lab1 = Label(self, text='  Chayan Sharma, Aditya Jha, Gaurav Gupta and Samriddhi Bhasin', font=('Verdana', 10), fg='darkblue', width=81 )
        lab1.pack()


        bottom = Frame()
        bottom.pack()
        but = Button(bottom, text='NEW USER', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=24,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.open1)
        but.pack(side='left')
        but = Button(bottom, text='EXISTING USER', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=24
                     , cursor='hand2',
                     activebackground='#86cc64', command=self.open2)
        but.pack(side='right')

    def open1(self, *arg):    # giving path to button New User to different class win2()
        self.destroy()
        win2().mainloop()

    def open2(self, *arg):     # giving path to button Existing User to different class win2()
        self.destroy()
        root = Tk()
        clas = login(root)
        win1.new = clas.user
        existing(win1.new).mainloop()


class win2(Tk):

    def __init__(self, *arg):
        Tk.__init__(self, *arg)

        self.lab1 = Label(text='ENTER YOUR DETAILS FOR NEW ID', font=('Times', 17, 'bold'), fg='#15633b')
        self.lab1.grid(row=1, column=1, columnspan=2)

        self.lab2 = Label(text='Username', font=('Times', 17), fg='#14b863')
        self.lab2.grid(row=2, column=1)
        self.txt1 = Entry(bd=4, width=20, font=('Verdana', 12))
        self.txt1.grid(row=2, column=2)

        self.lab3 = Label(text='Password', font=('Times', 17), fg='#14b863')
        self.lab3.grid(row=3, column=1)
        self.txt2 = Entry(bd=5, width=20, font=('Verdana', 12), show='*')
        self.txt2.grid(row=3, column=2)

        self.lab4 = Label(text='Contact No.', font=('Times', 17), fg='#14b863')
        self.lab4.grid(row=4, column=1)
        self.txt3 = Entry(bd=5, width=20, font=('Verdana', 12))
        self.txt3.grid(row=4, column=2)

        self.lab5 = Label(text='City', font=('Times', 17), fg='#14b863')
        self.lab5.grid(row=5, column=1)
        self.txt4 = Entry(bd=5, width=20, font=('Verdana', 12))
        self.txt4.grid(row=5, column=2)

        self.lab6 = Label(text='Email', font=('Times', 17), fg='#14b863')
        self.lab6.grid(row=6, column=1)
        self.txt5 = Entry(bd=5, width=20, font=('Verdana', 12))
        
        
        self.txt5.grid(row=6, column=2)

        self.txt1.bind('<Return>', self.call2)
        self.txt2.bind('<Return>', self.call3)
        self.txt3.bind('<Return>', self.call4)
        self.txt4.bind('<Return>', self.call5)
        self.txt5.bind('<Return>', self.call6)

        self.but = Button(self, text='BACK', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=15,
                          cursor='hand2',
                          activebackground='#86cc64', command=self.back)
        self.but.grid(row=7, column=1)
        self.but = Button(self, text='DONE', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=15,
                          cursor='hand2',
                          activebackground='#86cc64', command=self.done)
        self.but.grid(row=7, column=2)
        self.txt1.focus_set()

    def call2(self, *arg):
        return self.txt2.focus_set()

    def call3(self, *arg):
        return self.txt3.focus_set()

    def call4(self, *arg):
        return self.txt4.focus_set()

    def call5(self, *arg):
        return self.txt5.focus_set()

    def call6(self, *arg):
        return self.but.invoke()

    def done(self, *arg):   #Helping to Check wheather Inputs are valid or not
        self.user = self.txt1.get()
        if self.user == '':
            return tkmessagebox.showinfo('Error', 'Enter a username')
        self.password = self.txt2.get()
        if self.password == '':
            return tkmessagebox.showinfo('Error', 'Enter a password')
        self.contact = self.txt3.get()
        if self.contact == '':
            return tkmessagebox.showinfo('Error', 'Enter a contact')
        try:
            tmp = self.contact
            int(tmp)
        except ValueError:
            return tkmessagebox.showinfo('Error', 'Contact No. Should Be Integer')
        self.city = self.txt4.get()
        if self.user == '':
            return tkmessagebox.showinfo('Error', 'Enter a city')
        self.email = self.txt5.get()
        if self.user == '':
            return tkmessagebox.showinfo('Error', 'Enter an email')
        f = open('users.log', 'rb')
        while True:
            try:
                user = pickle.load(f)
                if user.name == self.user:
                    return tkmessagebox.showinfo('Error', 'Username Already Exists')

            except EOFError:
                f.close()
                break

        f = open('users.log', 'ab')
        new = new_file(name=self.user, password=self.password, contact=self.contact, city=self.city, email=self.email)
        pickle.dump(new, f)
        f.close()
        self.back()

    def back(self):
        self.destroy()
        win1()
class new_file(object):           
    def __init__(self, name, password, city, email, contact):
        self.name = name
        self.password = password
        self.city = city
        self.email = email
        self.contact = contact





class login():                        # Loign acess to software
    def __init__(self, root):
        self.users = {}
        self.root = root
        f = open('users.log', 'rb')
        while True:
            try:
                user = pickle.load(f)
                self.users[user.name] = user.password

            except EOFError:
                f.close
                break

        self.cont = Frame(self.root)
        self.cont.pack()
        self.name = StringVar()
        self.pasw = StringVar()
        self.head = Label(self.cont, text='LOGIN', font=('Times', 45, 'bold'), fg='#546775')
        self.head.grid(row=1, column=1, columnspan=2)
        self.lab1 = Label(self.cont, text='USERNAME', font=('Courier', 15, 'bold'), fg='#792834')
        self.lab1.grid(row=2, column=1)
        self.ent1 = Entry(self.cont, bd=5, font=('Courier', 15, 'bold'), textvariable=self.name)
        self.ent1.grid(row=2, column=2)
        self.ent1.focus_set()
        self.lab2 = Label(self.cont, text='PASSWORD', font=('Courier', 15, 'bold'), fg='#792834')
        self.lab2.grid(row=3, column=1)
        self.ent2 = Entry(self.cont, bd=5, font=('Courier', 15, 'bold'), show='*', textvariable=self.pasw)
        self.ent2.grid(row=3, column=2)
        self.but = Button(self.cont, text='Login', font=('Courier', 25, 'bold'), fg='cyan', command=self.callback)
        self.but.grid(row=4, column=1, columnspan=2)

        self.ent1.bind('<Return>', self.move1)
        self.ent2.bind('<Return>', self.move2)
        self.root.mainloop()

    def move1(self, *arg):
        return self.ent2.focus_set()

    def move2(self, *arg):
        return self.but.invoke()

    def callback(self):
        complete = False
        for user in self.users:
            if self.name.get() == user and self.pasw.get() == self.users[user]:
                complete = True
                self.root.destroy()
                self.user = user
                return
        if not complete:
            com = tkmessagebox.askyesno(title='Wrong Password', message='WRONG PASSWORD!!!!  Do you want to retry?')
            if com:
                self.ent2.delete(0, END)
            else:
                self.root.destroy()
                win1.win1()


class existing(Tk):       
    def __init__(self, name, *arg):
        Tk.__init__(self, *arg)
        self.name = name
        lab1 = Label(self, text='Welcome', font=('Comic Sans MS', 20), fg='black')
        lab1.pack()
        lab2 = Label(self, text='Mr.' + name, font=('Comic Sans MS', 50, 'bold'), fg='Dark Blue', width=13)
        lab2.pack()
        bottom = Frame()
        bottom.pack()
        
        
        
        but = Button(bottom, text='Blood Bank', font=('Courier', 20, 'bold'), fg='#436632', bg='#abcdef', width=20,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.open1)
        but.grid(row=1, column=1)

        but = Button(bottom, text='Modify Details', font=('Courier', 20, 'bold'), fg='#436632', bg='#abcdef', width=20,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.open2)
        but.grid(row=1, column=2)
        
        
        but = Button(bottom, text='Delete User', font=('Courier', 20, 'bold'), fg='#436632', bg='#abcdef', width=20,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.open3)
        but.grid(row=2, column=1)

        but = Button(bottom, text='   Prediction  ', font=('Courier', 20, 'bold'), fg='#436632', bg='#bbcdef', width=12,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.open5)
        but.grid(row=2, column=2)
        
        
        but = Button(bottom, text='   Back  ', font=('Courier', 20, 'bold'), fg='#436632', bg='#bbcdef', width=12,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.back)
        but.grid(row=3, column=1, columnspan=2 )
        
        
    def open1(self):
        self.destroy()
        Blood().mainloop()

    def open2(self, *arg):
        self.destroy()
        change(self.name).mainloop()
        


    def open3(self, *arg):
        self.destroy()
        f = open('users.log', 'rb')
        fn = open('temp.log', 'wb')
        while True:
            try:
                user = pickle.load(f)
                if win1.new != user.name:
                    pickle.dump(user, fn)

            except EOFError:
                f.close()
                fn.close()
                break

    def open4(self, *arg):
        self.destroy()
        os.remove('users.log')
        os.rename('temp.log', 'users.log')
        win1().mainloop()
        
    def open5(self):
        self.destroy()
        Prediction().mainloop()
    
   

    def back(self):
        self.destroy()
        win1().mainloop()


class change(Tk):
    def __init__(self, new, *arg):
        if new == None:
            return
        Tk.__init__(self, *arg)
        f = open('users.log', 'rb')
        self.new = new
        self.name = StringVar()
        self.pasw = StringVar()
        self.contact = StringVar()
        self.city = StringVar()
        self.email = StringVar()
        while True:
            try:
                user = pickle.load(f)
                if new == user.name:
                    self.name.set(user.name)
                    self.pasw.set(user.password)
                    self.city.set(user.city)
                    self.email.set(user.email)


            except EOFError:
                f.close()
                break

        self.lab1 = Label(text='UPDATE YOUR DETAILS U WANT TO CHANGE', font=('Times', 17, 'bold'), fg='#15633b')
        self.lab1.grid(row=1, column=1, columnspan=2)

        self.lab2 = Label(text='Username', font=('Times', 17), fg='#14b863')
        self.lab2.grid(row=2, column=1)
        self.txt1 = Entry(bd=4, width=20, font=('Verdana', 12), textvariable=self.name)
        self.txt1.grid(row=2, column=2)

        self.lab3 = Label(text='Password', font=('Times', 17), fg='#14b863')
        self.lab3.grid(row=3, column=1)
        self.txt2 = Entry(bd=5, width=20, font=('Verdana', 12), textvariable=self.pasw)
        self.txt2.grid(row=3, column=2)




        self.lab4 = Label(text='Contact No.', font=('Times', 17), fg='#14b863')
        self.lab4.grid(row=4, column=1)
        self.txt3 = Entry(bd=5, width=20, font=('Verdana', 12), textvariable=self.contact)
        self.txt3.grid(row=4, column=2)

        self.lab5 = Label(text='City', font=('Times', 17), fg='#14b863')
        self.lab5.grid(row=5, column=1)
        self.txt4 = Entry(bd=5, width=20, font=('Verdana', 12), textvariable=self.city)
        self.txt4.grid(row=5, column=2)

        self.lab6 = Label(text='Email', font=('Times', 17), fg='#14b863')
        self.lab6.grid(row=6, column=1)
        self.txt5 = Entry(bd=5, width=20, font=('Verdana', 12), textvariable=self.email)
        self.txt5.grid(row=6, column=2)

        self.txt1.bind('<Return>', self.call2)
        self.txt2.bind('<Return>', self.call3)
        self.txt3.bind('<Return>', self.call4)
        self.txt4.bind('<Return>', self.call5)
        self.txt5.bind('<Return>', self.call6)
        self.but = Button(self, text='BACK', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=15,
                          cursor='hand2',
                          activebackground='#86cc64', command=self.back)
        self.but.grid(row=7, column=1)

        self.but = Button(self, text='DONE', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=15,
                          cursor='hand2',
                          activebackground='#86cc64', command=self.callback)
        self.but.grid(row=7, column=2)

    def call2(self, *arg):
        return self.txt2.focus_set()

    def call3(self, *arg):
        return self.txt3.focus_set()

    def call4(self, *arg):
        return self.txt4.focus_set()

    def call5(self, *arg):
        return self.txt5.focus_set()

    def call6(self, *arg):
        return self.but.invoke()

    def callback(self, *arg):
        f = open('users.log', 'rb')
        fn = open('temp.log', 'wb')
        while True:
            try:
                user = pickle.load(f)
                if self.new == user.name:
                    name = self.name.get()
                    pas = self.pasw.get()
                    contact = self.contact.get()
                    email = self.email.get()
                    city = self.city.get()
                    user = new_file(name, pas, city, email, contact)
                pickle.dump(user, fn)

            except EOFError:
                f.close()
                fn.close()
                break
        os.remove('users.log')
        os.rename('temp.log', 'users.log')
        self.back()

    def back(self):
        self.destroy()
        existing(win1.new).mainloop()
        
        
       
        
        
class Blood(Tk):      

    def __init__(self):        
        Tk.__init__(self)
        lab1 = Label(self, text='Blood Bank (Choose Blood Group)', font=('Comic Sans MS', 30), fg='red', width=30, bg='#000000')
        lab1.pack()
        bottom = Frame()
        bottom.pack()
        but1 = Button(bottom, text='A+', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.AP)
        but1.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        
        but2 = Button(bottom, text='B+', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.BP)
        but2.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        
        but3 = Button(bottom, text='AB+', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.ABP)
        but3.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        
        but4 = Button(bottom, text='O+', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.ON)
        but4.grid(row=1, column=1)


        bottom = Frame()
        bottom.pack()
        
        but5 = Button(bottom, text='A-', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.AN)
        but5.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        
        but6 = Button(bottom, text='B-', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.BN)
        but6.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        
        but7 = Button(bottom, text='AB-', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.ABN)
        but7.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        but8 = Button(bottom, text='O-', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.ON)
        but8.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()

        but12 = Button(bottom, text='Back', font=('Courier', 10, 'bold'), fg='#006400', bg='#000000', width=30,
                       cursor='hand2',
                       activebackground='#86cc64', command=self.back)
        but12.grid(row=1, column=1)
        
        bottom = Frame()
        bottom.pack()

     
        
    def AP(self, *arg):            
        df = pandas.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\Blood Bank.csv")
        df.head()
        type(df)
        df.shape        
        a=df[["HNAME","Location","Distance(in kms)"]][(df["A+"]>15) & (df["Distance(in kms)"]<10) & (df["Review1"]>=3) & (df["Review2"]>=3)]
        #print(a)
        root = tk.Tk()
        T = tk.Text(root, height=40, width=800)
        T.pack()
        T.insert(tk.END,a)
        #tex.see(tk.END)
       
    
        


        tk.mainloop()
        self.back()
    
    def BP(self, *arg):        
        df = pandas.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\Blood Bank.csv")
        df.head()
        type(df)
        df.shape          
        a=df[["HNAME","Location","Distance(in kms)"]][(df["B+"]>15) & (df["Distance(in kms)"]<10) & (df["Review1"]>=3) & (df["Review2"]>=3)]
        #print(a)
        root = tk.Tk()
        T = tk.Text(root, height=40, width=800)
        T.pack()
        T.insert(tk.END,a)
        #tex.see(tk.END)
        
        


        tk.mainloop()
        self.back()
    

    def ABP(self, *arg):             
        df = pandas.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\Blood Bank.csv")
        df.head()
        type(df)
        df.shape          
        a=df[["HNAME","Location","Distance(in kms)"]][(df["AB+"]>15) & (df["Distance(in kms)"]<10) & (df["Review1"]>=3) & (df["Review2"]>=3)]
        #print(a)
        root = tk.Tk()
        T = tk.Text(root, height=40, width=800)
        T.pack()
        T.insert(tk.END,a)
        #tex.see(tk.END)    
        


        tk.mainloop()
        self.back()
    
    
    def OP(self, *arg):             
        df = pandas.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\Blood Bank.csv")
        df.head()
        type(df)
        df.shape          
        a=df[["HNAME","Location","Distance(in kms)"]][(df["O+"]>15) & (df["Distance(in kms)"]<10) & (df["Review1"]>=3) & (df["Review2"]>=3)]
        #print(a)
        root = tk.Tk()
        T = tk.Text(root, height=40, width=800)
        T.pack()
        T.insert(tk.END,a)
        #tex.see(tk.END)
        


        tk.mainloop()
        self.back()
    
    def AN(self, *arg):
        df = pandas.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\Blood Bank.csv")
        df.head()
        type(df)
        df.shape          
        a=df[["HNAME","Location","Distance(in kms)"]][(df["A-"]>15) & (df["Distance(in kms)"]<10) & (df["Review1"]>=3) & (df["Review2"]>=3)]
        #print(a)
        root = tk.Tk()
        T = tk.Text(root, height=40, width=800)
        T.pack()
        T.insert(tk.END,a)
        #tex.see(tk.END)
    
        


        tk.mainloop()
        self.back()
            
        
    def BN(self, *arg):
        df = pandas.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\Blood Bank.csv")
        df.head()
        type(df)
        df.shape          
        a=df[["HNAME","Location","Distance(in kms)"]][(df["B-"]>15) & (df["Distance(in kms)"]<10) & (df["Review1"]>=3) & (df["Review2"]>=3)]
        #print(a)
        root = tk.Tk()
        T = tk.Text(root, height=40, width=800)
        T.pack()
        T.insert(tk.END,a)
        #tex.see(tk.END)
    
        


        tk.mainloop()
        self.back()
    
    def ABN(self, *arg):            
        df = pandas.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\Blood Bank.csv")
        df.head()
        type(df)
        df.shape      
        a=df[["HNAME","Location","Distance(in kms)"]][(df["AB-"]>15) & (df["Distance(in kms)"]<10) & (df["Review1"]>=3) & (df["Review2"]>=3)]
        print(a)
        root = tk.Tk()
        T = tk.Text(root, height=40, width=800)
        T.pack()
        T.insert(tk.END,a)
        #tex.see(tk.END)
        
    
        


        tk.mainloop()
        self.back()
    
    def ON(self, *arg):             
        df = pandas.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\Blood Bank.csv")
        df.head()
        type(df)
        df.shape          
        a=df[["HNAME","Location","Distance(in kms)"]][(df["O-"]>15) & (df["Distance(in kms)"]<10) & (df["Review1"]>=3) & (df["Review2"]>=3)]
        #print(a)
        root = tk.Tk()
        T = tk.Text(root, height=40, width=800)
        T.pack()
        T.insert(tk.END,a)
        #tex.see(tk.END)
        


        tk.mainloop()
        self.back()
    
        
        
    def back(self):
        self.destroy()
        win1()
        
class Prediction(Tk):

    
    
    def __init__(self):        
        Tk.__init__(self)
        
        lab1 = Label(self, text='Preditions', font=('Comic Sans MS', 50), fg='red', width=13, bg='#000000')
        lab1.pack()
        bottom = Frame()
        bottom.pack()
        but1 = Button(bottom, text='A+', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.a)
        but1.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        
        but2 = Button(bottom, text='B+', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.b)
        but2.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        
        but3 = Button(bottom, text='AB+', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.ab)
        but3.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        
        but4 = Button(bottom, text='O+', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.o)
        but4.grid(row=1, column=1)


        bottom = Frame()
        bottom.pack()
        
        but5 = Button(bottom, text='A-', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.ane)
        but5.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        
        but6 = Button(bottom, text='B-', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.bne)
        but6.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        
        but7 = Button(bottom, text='AB-', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.abne)
        but7.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        but8 = Button(bottom, text='O-', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.one)
        but8.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()

        but9 = Button(bottom, text='Back', font=('Courier', 10, 'bold'), fg='#006400', bg='#000000', width=30,
                       cursor='hand2',
                       activebackground='#86cc64', command=self.back)
        but9.grid(row=1, column=1)
        
        bottom = Frame()
        bottom.pack()
   
    def a(self, *arg):
        traindata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\apov (1).csv ",delimiter=",")
        testdata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\apovtest.csv",delimiter=",")
        
        df=pd.DataFrame(traindata)
        
        xtrain=df.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtrain.shape
        y1train=df["All India Institute of Medical Sciences (AIIMS)"]
        y1train
        y2train=df["Armed Forces Transfusion Centre"]
        y3train=df["Dr. Ram Manohar Lohia Hospital"]
        y4train=df["E.S.I. Hospital"]
        y5train=df["Safdarjung Hospital"]
        y6train=df["Sucheta Kriplani Hospital"]
        y7train=df["Govind Ballabh Pant Hospital"]
        y8train=df["Guru Tegh Bahadur Hospital"]
        y9train=df["Regional Blood tranfusion Center of Central zone"]
        df2=pd.DataFrame(testdata)
        xtest=df2.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtest.shape
        y1test=df2["All India Institute of Medical Sciences (AIIMS)"]
        y1test
        y2test=df2["Armed Forces Transfusion Centre"]
        y3test=df2["Dr. Ram Manohar Lohia Hospital"]
        y4test=df2["E.S.I. Hospital"]
        y5test=df2["Safdarjung Hospital"]
        y6test=df2["Sucheta Kriplani Hospital"]
        y7test=df2["Govind Ballabh Pant Hospital"]
        y8test=df2["Guru Tegh Bahadur Hospital"]
        y9test=df2["Regional Blood tranfusion Center of Central zone"]
        cl=RandomForestClassifier(random_state=0)
        cl.fit(xtrain,y1train)
        ypred1=cl.predict(xtest)
        print(ypred1)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP A+ In AIIMS IS")
        w=(accuracy_score(y1test, ypred1))
        print(w*100)
        
        c=RandomForestClassifier(random_state=0)
        c.fit(xtrain,y2train)
        ypred2=c.predict(xtest)
        print(ypred2)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP A+ In ARMED FORCES IS")
        p=(accuracy_score(y2test, ypred2))
        print(p*100)
        
        l=RandomForestClassifier(random_state=0)
        l.fit(xtrain,y3train)
        ypred3=l.predict(xtest)
        print(ypred3)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A+ In ram hospital IS")
        q=(accuracy_score(y3test, ypred3))
        print(q*100)

        u=RandomForestClassifier(random_state=0)
        u.fit(xtrain,y4train)
        ypred4=u.predict(xtest)
        print(ypred4)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A+ In ESI hospital IS")
        g=(accuracy_score(y4test, ypred4))
        print(g*100)
        
        a=RandomForestClassifier(random_state=0)
        a.fit(xtrain,y5train)
        ypred5=a.predict(xtest)
        print(ypred5)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A+ In sarfdung hospital IS")
        h=(accuracy_score(y5test, ypred5))
        print(h*100)
        
        b=RandomForestClassifier(random_state=0)
        b.fit(xtrain,y6train)
        ypred6=b.predict(xtest)
        print(ypred6)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A+ In SUCHETA KRIPLANI hospital IS")
        i=(accuracy_score(y6test, ypred6))
        print(i*100)

        y=RandomForestClassifier(random_state=0)
        y.fit(xtrain,y7train)
        ypred7=y.predict(xtest)
        print(ypred7)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A+ In GOVIND BALLABH PANT hospital IS")
        j=(accuracy_score(y7test, ypred7))
        print(j*100)
        
        
        lr=RandomForestClassifier(random_state=0)
        lr.fit(xtrain,y8train)
        ypred8=lr.predict(xtest)
        print(ypred8)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A+ In GURU TEGH BAHADUR hospital IS")
        hg=(accuracy_score(y8test, ypred8))
        print(hg*100)
        
        clr=RandomForestClassifier(random_state=0)
        clr.fit(xtrain,y9train)
        ypred9=clr.predict(xtest)
        print(ypred9)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A+ In REGIONAL BLOOD TRANFUSION CENTRE CENTRAL ZONE  hospital IS")
        hge=(accuracy_score(y9test, ypred9))
        print(hge*100)


        
        
        
        tk.mainloop()
        self.back()
        
        


    def b(self, *arg):
        
        traindata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\bpov (1).csv ",delimiter=",")
        testdata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\bpovtest.csv",delimiter=",")
        
        df=pd.DataFrame(traindata)
        
        xtrain=df.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtrain.shape
        y1train=df["All India Institute of Medical Sciences (AIIMS)"]
        y1train
        y2train=df["Armed Forces Transfusion Centre"]
        y3train=df["Dr. Ram Manohar Lohia Hospital"]
        y4train=df["E.S.I. Hospital"]
        y5train=df["Safdarjung Hospital"]
        y6train=df["Sucheta Kriplani Hospital"]
        y7train=df["Govind Ballabh Pant Hospital"]
        y8train=df["Guru Tegh Bahadur Hospital"]
        y9train=df["Regional Blood tranfusion Center of Central zone"]
        df2=pd.DataFrame(testdata)
        xtest=df2.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtest.shape
        y1test=df2["All India Institute of Medical Sciences (AIIMS)"]
        y1test
        y2test=df2["Armed Forces Transfusion Centre"]
        y3test=df2["Dr. Ram Manohar Lohia Hospital"]
        y4test=df2["E.S.I. Hospital"]
        y5test=df2["Safdarjung Hospital"]
        y6test=df2["Sucheta Kriplani Hospital"]
        y7test=df2["Govind Ballabh Pant Hospital"]
        y8test=df2["Guru Tegh Bahadur Hospital"]
        y9test=df2["Regional Blood tranfusion Center of Central zone"]
        cl=RandomForestClassifier(random_state=0)
        cl.fit(xtrain,y1train)
        ypred1=cl.predict(xtest)
        print(ypred1)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP B+ In AIIMS IS")
        w=(accuracy_score(y1test, ypred1))
        print(w*100)
        
        c=RandomForestClassifier(random_state=0)
        c.fit(xtrain,y2train)
        ypred2=c.predict(xtest)
        print(ypred2)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP B+ In ARMED FORCES IS")
        p=(accuracy_score(y2test, ypred2))
        print(p*100)
        
        l=RandomForestClassifier(random_state=0)
        l.fit(xtrain,y3train)
        ypred3=l.predict(xtest)
        print(ypred3)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B+ In ram hospital IS")
        q=(accuracy_score(y3test, ypred3))
        print(q*100)

        u=RandomForestClassifier(random_state=0)
        u.fit(xtrain,y4train)
        ypred4=u.predict(xtest)
        print(ypred4)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B+ In ESI hospital IS")
        g=(accuracy_score(y4test, ypred4))
        print(g*100)
        
        a=RandomForestClassifier(random_state=0)
        a.fit(xtrain,y5train)
        ypred5=a.predict(xtest)
        print(ypred5)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B+ In sarfdung hospital IS")
        h=(accuracy_score(y5test, ypred5))
        print(h*100)
        
        b=RandomForestClassifier(random_state=0)
        b.fit(xtrain,y6train)
        ypred6=b.predict(xtest)
        print(ypred6)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B+ In SUCHETA KRIPLANI hospital IS")
        i=(accuracy_score(y6test, ypred6))
        print(i*100)

        y=RandomForestClassifier(random_state=0)
        y.fit(xtrain,y7train)
        ypred7=y.predict(xtest)
        print(ypred7)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B+ In GOVIND BALLABH PANT hospital IS")
        j=(accuracy_score(y7test, ypred7))
        print(j*100)
        
        
        lr=RandomForestClassifier(random_state=0)
        lr.fit(xtrain,y8train)
        ypred8=lr.predict(xtest)
        print(ypred8)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B+ In GURU TEGH BAHADUR hospital IS")
        hg=(accuracy_score(y8test, ypred8))
        print(hg*100)
        
        clr=RandomForestClassifier(random_state=0)
        clr.fit(xtrain,y9train)
        ypred9=clr.predict(xtest)
        print(ypred9)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B+ In REGIONAL BLOOD TRANFUSION CENTRE CENTRAL ZONE  hospital IS")
        hge=(accuracy_score(y9test, ypred9))
        print(hge*100)
        
        tk.mainloop()
        self.back()
        
        
        
    def ab(self, *arg):
        
        traindata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\abpov (1).csv ",delimiter=",")
        testdata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\abpovtest.csv",delimiter=",")
        
        df=pd.DataFrame(traindata)
        
        xtrain=df.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtrain.shape
        y1train=df["All India Institute of Medical Sciences (AIIMS)"]
        y1train
        y2train=df["Armed Forces Transfusion Centre"]
        y3train=df["Dr. Ram Manohar Lohia Hospital"]
        y4train=df["E.S.I. Hospital"]
        y5train=df["Safdarjung Hospital"]
        y6train=df["Sucheta Kriplani Hospital"]
        y7train=df["Govind Ballabh Pant Hospital"]
        y8train=df["Guru Tegh Bahadur Hospital"]
        y9train=df["Regional Blood tranfusion Center of Central zone"]
        df2=pd.DataFrame(testdata)
        xtest=df2.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtest.shape
        y1test=df2["All India Institute of Medical Sciences (AIIMS)"]
        y1test
        y2test=df2["Armed Forces Transfusion Centre"]
        y3test=df2["Dr. Ram Manohar Lohia Hospital"]
        y4test=df2["E.S.I. Hospital"]
        y5test=df2["Safdarjung Hospital"]
        y6test=df2["Sucheta Kriplani Hospital"]
        y7test=df2["Govind Ballabh Pant Hospital"]
        y8test=df2["Guru Tegh Bahadur Hospital"]
        y9test=df2["Regional Blood tranfusion Center of Central zone"]
        cl=RandomForestClassifier(random_state=0)
        cl.fit(xtrain,y1train)
        ypred1=cl.predict(xtest)
        print(ypred1)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP AB+ In AIIMS IS")
        w=(accuracy_score(y1test, ypred1))
        print(w*100)
        
        c=RandomForestClassifier(random_state=0)
        c.fit(xtrain,y2train)
        ypred2=c.predict(xtest)
        print(ypred2)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP AB+ In ARMED FORCES IS")
        p=(accuracy_score(y2test, ypred2))
        print(p*100)
        
        l=RandomForestClassifier(random_state=0)
        l.fit(xtrain,y3train)
        ypred3=l.predict(xtest)
        print(ypred3)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB+ In ram hospital IS")
        q=(accuracy_score(y3test, ypred3))
        print(q*100)

        u=RandomForestClassifier(random_state=0)
        u.fit(xtrain,y4train)
        ypred4=u.predict(xtest)
        print(ypred4)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB+ In ESI hospital IS")
        g=(accuracy_score(y4test, ypred4))
        print(g*100)
        
        a=RandomForestClassifier(random_state=0)
        a.fit(xtrain,y5train)
        ypred5=a.predict(xtest)
        print(ypred5)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB+ In sarfdung hospital IS")
        h=(accuracy_score(y5test, ypred5))
        print(h*100)
        
        b=RandomForestClassifier(random_state=0)
        b.fit(xtrain,y6train)
        ypred6=b.predict(xtest)
        print(ypred6)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB+ In SUCHETA KRIPLANI hospital IS")
        i=(accuracy_score(y6test, ypred6))
        print(i*100)

        y=RandomForestClassifier(random_state=0)
        y.fit(xtrain,y7train)
        ypred7=y.predict(xtest)
        print(ypred7)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB+ In GOVIND BALLABH PANT hospital IS")
        j=(accuracy_score(y7test, ypred7))
        print(j*100)
        
        
        lr=RandomForestClassifier(random_state=0)
        lr.fit(xtrain,y8train)
        ypred8=lr.predict(xtest)
        print(ypred8)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB+ In GURU TEGH BAHADUR hospital IS")
        hg=(accuracy_score(y8test, ypred8))
        print(hg*100)
        
        clr=RandomForestClassifier(random_state=0)
        clr.fit(xtrain,y9train)
        ypred9=clr.predict(xtest)
        print(ypred9)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB+ In REGIONAL BLOOD TRANFUSION CENTRE CENTRAL ZONE  hospital IS")
        hge=(accuracy_score(y9test, ypred9))
        print(hge*100)
        

        tk.mainloop()
        self.back()
        
    def o(self, *arg):
        traindata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\opov.csv ",delimiter=",")
        testdata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\opovtest.csv",delimiter=",")
        
        df=pd.DataFrame(traindata)
        
        xtrain=df.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtrain.shape
        y1train=df["All India Institute of Medical Sciences (AIIMS)"]
        y1train
        y2train=df["Armed Forces Transfusion Centre"]
        y3train=df["Dr. Ram Manohar Lohia Hospital"]
        y4train=df["E.S.I. Hospital"]
        y5train=df["Safdarjung Hospital"]
        y6train=df["Sucheta Kriplani Hospital"]
        y7train=df["Govind Ballabh Pant Hospital"]
        y8train=df["Guru Tegh Bahadur Hospital"]
        y9train=df["Regional Blood tranfusion Center of Central zone"]
        df2=pd.DataFrame(testdata)
        xtest=df2.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtest.shape
        y1test=df2["All India Institute of Medical Sciences (AIIMS)"]
        y1test
        y2test=df2["Armed Forces Transfusion Centre"]
        y3test=df2["Dr. Ram Manohar Lohia Hospital"]
        y4test=df2["E.S.I. Hospital"]
        y5test=df2["Safdarjung Hospital"]
        y6test=df2["Sucheta Kriplani Hospital"]
        y7test=df2["Govind Ballabh Pant Hospital"]
        y8test=df2["Guru Tegh Bahadur Hospital"]
        y9test=df2["Regional Blood tranfusion Center of Central zone"]
        cl=RandomForestClassifier(random_state=0)
        cl.fit(xtrain,y1train)
        ypred1=cl.predict(xtest)
        print(ypred1)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP O+ In AIIMS IS")
        w=(accuracy_score(y1test, ypred1))
        print(w*100)
        
        c=RandomForestClassifier(random_state=0)
        c.fit(xtrain,y2train)
        ypred2=c.predict(xtest)
        print(ypred2)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP O+ In ARMED FORCES IS")
        p=(accuracy_score(y2test, ypred2))
        print(p*100)
        
        l=RandomForestClassifier(random_state=0)
        l.fit(xtrain,y3train)
        ypred3=l.predict(xtest)
        print(ypred3)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O+ In ram hospital IS")
        q=(accuracy_score(y3test, ypred3))
        print(q*100)

        u=RandomForestClassifier(random_state=0)
        u.fit(xtrain,y4train)
        ypred4=u.predict(xtest)
        print(ypred4)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O+ In ESI hospital IS")
        g=(accuracy_score(y4test, ypred4))
        print(g*100)
        
        a=RandomForestClassifier(random_state=0)
        a.fit(xtrain,y5train)
        ypred5=a.predict(xtest)
        print(ypred5)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O+ In sarfdung hospital IS")
        h=(accuracy_score(y5test, ypred5))
        print(h*100)
        
        b=RandomForestClassifier(random_state=0)
        b.fit(xtrain,y6train)
        ypred6=b.predict(xtest)
        print(ypred6)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O+ In SUCHETA KRIPLANI hospital IS")
        i=(accuracy_score(y6test, ypred6))
        print(i*100)

        y=RandomForestClassifier(random_state=0)
        y.fit(xtrain,y7train)
        ypred7=y.predict(xtest)
        print(ypred7)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O+ In GOVIND BALLABH PANT hospital IS")
        j=(accuracy_score(y7test, ypred7))
        print(j*100)
        
        
        lr=RandomForestClassifier(random_state=0)
        lr.fit(xtrain,y8train)
        ypred8=lr.predict(xtest)
        print(ypred8)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O+ In GURU TEGH BAHADUR hospital IS")
        hg=(accuracy_score(y8test, ypred8))
        print(hg*100)
        
        clr=RandomForestClassifier(random_state=0)
        clr.fit(xtrain,y9train)
        ypred9=clr.predict(xtest)
        print(ypred9)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O+ In REGIONAL BLOOD TRANFUSION CENTRE CENTRAL ZONE  hospital IS")
        hge=(accuracy_score(y9test, ypred9))
        print(hge*100)
        
        tk.mainloop()
        self.back()

    def one(self, *arg):
        
        traindata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\oneg (1).csv ",delimiter=",")
        testdata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\onegtest.csv",delimiter=",")
        
        df=pd.DataFrame(traindata)
        
        xtrain=df.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtrain.shape
        y1train=df["All India Institute of Medical Sciences (AIIMS)"]
        y1train
        y2train=df["Armed Forces Transfusion Centre"]
        y3train=df["Dr. Ram Manohar Lohia Hospital"]
        y4train=df["E.S.I. Hospital"]
        y5train=df["Safdarjung Hospital"]
        y6train=df["Sucheta Kriplani Hospital"]
        y7train=df["Govind Ballabh Pant Hospital"]
        y8train=df["Guru Tegh Bahadur Hospital"]
        y9train=df["Regional Blood tranfusion Center of Central zone"]
        df2=pd.DataFrame(testdata)
        xtest=df2.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtest.shape
        y1test=df2["All India Institute of Medical Sciences (AIIMS)"]
        y1test
        y2test=df2["Armed Forces Transfusion Centre"]
        y3test=df2["Dr. Ram Manohar Lohia Hospital"]
        y4test=df2["E.S.I. Hospital"]
        y5test=df2["Safdarjung Hospital"]
        y6test=df2["Sucheta Kriplani Hospital"]
        y7test=df2["Govind Ballabh Pant Hospital"]
        y8test=df2["Guru Tegh Bahadur Hospital"]
        y9test=df2["Regional Blood tranfusion Center of Central zone"]
        cl=RandomForestClassifier(random_state=0)
        cl.fit(xtrain,y1train)
        ypred1=cl.predict(xtest)
        print(ypred1)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP O- In AIIMS IS")
        w=(accuracy_score(y1test, ypred1))
        print(w*100)
        
        c=RandomForestClassifier(random_state=0)
        c.fit(xtrain,y2train)
        ypred2=c.predict(xtest)
        print(ypred2)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP O- In ARMED FORCES IS")
        p=(accuracy_score(y2test, ypred2))
        print(p*100)
        
        l=RandomForestClassifier(random_state=0)
        l.fit(xtrain,y3train)
        ypred3=l.predict(xtest)
        print(ypred3)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O- In ram hospital IS")
        q=(accuracy_score(y3test, ypred3))
        print(q*100)

        u=RandomForestClassifier(random_state=0)
        u.fit(xtrain,y4train)
        ypred4=u.predict(xtest)
        print(ypred4)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O- In ESI hospital IS")
        g=(accuracy_score(y4test, ypred4))
        print(g*100)
        
        a=RandomForestClassifier(random_state=0)
        a.fit(xtrain,y5train)
        ypred5=a.predict(xtest)
        print(ypred5)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O- In sarfdung hospital IS")
        h=(accuracy_score(y5test, ypred5))
        print(h*100)
        
        b=RandomForestClassifier(random_state=0)
        b.fit(xtrain,y6train)
        ypred6=b.predict(xtest)
        print(ypred6)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O- In SUCHETA KRIPLANI hospital IS")
        i=(accuracy_score(y6test, ypred6))
        print(i*100)

        y=RandomForestClassifier(random_state=0)
        y.fit(xtrain,y7train)
        ypred7=y.predict(xtest)
        print(ypred7)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O- In GOVIND BALLABH PANT hospital IS")
        j=(accuracy_score(y7test, ypred7))
        print(j*100)
        
        
        lr=RandomForestClassifier(random_state=0)
        lr.fit(xtrain,y8train)
        ypred8=lr.predict(xtest)
        print(ypred8)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O- In GURU TEGH BAHADUR hospital IS")
        hg=(accuracy_score(y8test, ypred8))
        print(hg*100)
        
        clr=RandomForestClassifier(random_state=0)
        clr.fit(xtrain,y9train)
        ypred9=clr.predict(xtest)
        print(ypred9)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP O- In REGIONAL BLOOD TRANFUSION CENTRE CENTRAL ZONE  hospital IS")
        hge=(accuracy_score(y9test, ypred9))
        print(hge*100)
        
        
        tk.mainloop()
        self.back()
    
    def abne(self, *arg):
        
        traindata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\abneg (1).csv ",delimiter=",")
        testdata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\abnegtest.csv",delimiter=",")
        df=pd.DataFrame(traindata)
        
        xtrain=df.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtrain.shape
        y1train=df["All India Institute of Medical Sciences (AIIMS)"]
        y1train
        y2train=df["Armed Forces Transfusion Centre"]
        y3train=df["Dr. Ram Manohar Lohia Hospital"]
        y4train=df["E.S.I. Hospital"]
        y5train=df["Safdarjung Hospital"]
        y6train=df["Sucheta Kriplani Hospital"]
        y7train=df["Govind Ballabh Pant Hospital"]
        y8train=df["Guru Tegh Bahadur Hospital"]
        y9train=df["Regional Blood tranfusion Center of Central zone"]
        df2=pd.DataFrame(testdata)
        xtest=df2.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtest.shape
        y1test=df2["All India Institute of Medical Sciences (AIIMS)"]
        y1test
        y2test=df2["Armed Forces Transfusion Centre"]
        y3test=df2["Dr. Ram Manohar Lohia Hospital"]
        y4test=df2["E.S.I. Hospital"]
        y5test=df2["Safdarjung Hospital"]
        y6test=df2["Sucheta Kriplani Hospital"]
        y7test=df2["Govind Ballabh Pant Hospital"]
        y8test=df2["Guru Tegh Bahadur Hospital"]
        y9test=df2["Regional Blood tranfusion Center of Central zone"]
        cl=RandomForestClassifier(random_state=0)
        cl.fit(xtrain,y1train)
        ypred1=cl.predict(xtest)
        print(ypred1)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP AB- In AIIMS IS")
        w=(accuracy_score(y1test, ypred1))
        print(w*100)
        
        c=RandomForestClassifier(random_state=0)
        c.fit(xtrain,y2train)
        ypred2=c.predict(xtest)
        print(ypred2)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP AB- In ARMED FORCES IS")
        p=(accuracy_score(y2test, ypred2))
        print(p*100)
        
        l=RandomForestClassifier(random_state=0)
        l.fit(xtrain,y3train)
        ypred3=l.predict(xtest)
        print(ypred3)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB- In ram hospital IS")
        q=(accuracy_score(y3test, ypred3))
        print(q*100)

        u=RandomForestClassifier(random_state=0)
        u.fit(xtrain,y4train)
        ypred4=u.predict(xtest)
        print(ypred4)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB- In ESI hospital IS")
        g=(accuracy_score(y4test, ypred4))
        print(g*100)
        
        a=RandomForestClassifier(random_state=0)
        a.fit(xtrain,y5train)
        ypred5=a.predict(xtest)
        print(ypred5)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB- In sarfdung hospital IS")
        h=(accuracy_score(y5test, ypred5))
        print(h*100)
        
        b=RandomForestClassifier(random_state=0)
        b.fit(xtrain,y6train)
        ypred6=b.predict(xtest)
        print(ypred6)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB- In SUCHETA KRIPLANI hospital IS")
        i=(accuracy_score(y6test, ypred6))
        print(i*100)

        y=RandomForestClassifier(random_state=0)
        y.fit(xtrain,y7train)
        ypred7=y.predict(xtest)
        print(ypred7)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB- In GOVIND BALLABH PANT hospital IS")
        j=(accuracy_score(y7test, ypred7))
        print(j*100)
        
        
        lr=RandomForestClassifier(random_state=0)
        lr.fit(xtrain,y8train)
        ypred8=lr.predict(xtest)
        print(ypred8)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB- In GURU TEGH BAHADUR hospital IS")
        hg=(accuracy_score(y8test, ypred8))
        print(hg*100)
        
        clr=RandomForestClassifier(random_state=0)
        clr.fit(xtrain,y9train)
        ypred9=clr.predict(xtest)
        print(ypred9)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP AB- In REGIONAL BLOOD TRANFUSION CENTRE CENTRAL ZONE  hospital IS")
        hge=(accuracy_score(y9test, ypred9))
        print(hge*100)
        
        
        tk.mainloop()
        self.back()
        
    
    def ane(self, *arg):
        traindata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\aneg (1).csv ",delimiter=",")
        testdata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\anegtest.csv",delimiter=",")
        
        df=pd.DataFrame(traindata)
        
        xtrain=df.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtrain.shape
        y1train=df["All India Institute of Medical Sciences (AIIMS)"]
        y1train
        y2train=df["Armed Forces Transfusion Centre"]
        y3train=df["Dr. Ram Manohar Lohia Hospital"]
        y4train=df["E.S.I. Hospital"]
        y5train=df["Safdarjung Hospital"]
        y6train=df["Sucheta Kriplani Hospital"]
        y7train=df["Govind Ballabh Pant Hospital"]
        y8train=df["Guru Tegh Bahadur Hospital"]
        y9train=df["Regional Blood tranfusion Center of Central zone"]
        df2=pd.DataFrame(testdata)
        xtest=df2.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtest.shape
        y1test=df2["All India Institute of Medical Sciences (AIIMS)"]
        y1test
        y2test=df2["Armed Forces Transfusion Centre"]
        y3test=df2["Dr. Ram Manohar Lohia Hospital"]
        y4test=df2["E.S.I. Hospital"]
        y5test=df2["Safdarjung Hospital"]
        y6test=df2["Sucheta Kriplani Hospital"]
        y7test=df2["Govind Ballabh Pant Hospital"]
        y8test=df2["Guru Tegh Bahadur Hospital"]
        y9test=df2["Regional Blood tranfusion Center of Central zone"]
        cl=RandomForestClassifier(random_state=0)
        cl.fit(xtrain,y1train)
        ypred1=cl.predict(xtest)
        print(ypred1)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP A- In AIIMS IS")
        w=(accuracy_score(y1test, ypred1))
        print(w*100)
        
        c=RandomForestClassifier(random_state=0)
        c.fit(xtrain,y2train)
        ypred2=c.predict(xtest)
        print(ypred2)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP A- In ARMED FORCES IS")
        p=(accuracy_score(y2test, ypred2))
        print(p*100)
        
        l=RandomForestClassifier(random_state=0)
        l.fit(xtrain,y3train)
        ypred3=l.predict(xtest)
        print(ypred3)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A- In ram hospital IS")
        q=(accuracy_score(y3test, ypred3))
        print(q*100)

        u=RandomForestClassifier(random_state=0)
        u.fit(xtrain,y4train)
        ypred4=u.predict(xtest)
        print(ypred4)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A- In ESI hospital IS")
        g=(accuracy_score(y4test, ypred4))
        print(g*100)
        
        a=RandomForestClassifier(random_state=0)
        a.fit(xtrain,y5train)
        ypred5=a.predict(xtest)
        print(ypred5)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A- In sarfdung hospital IS")
        h=(accuracy_score(y5test, ypred5))
        print(h*100)
        
        b=RandomForestClassifier(random_state=0)
        b.fit(xtrain,y6train)
        ypred6=b.predict(xtest)
        print(ypred6)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A- In SUCHETA KRIPLANI hospital IS")
        i=(accuracy_score(y6test, ypred6))
        print(i*100)

        y=RandomForestClassifier(random_state=0)
        y.fit(xtrain,y7train)
        ypred7=y.predict(xtest)
        print(ypred7)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A- In GOVIND BALLABH PANT hospital IS")
        j=(accuracy_score(y7test, ypred7))
        print(j*100)
        
        
        lr=RandomForestClassifier(random_state=0)
        lr.fit(xtrain,y8train)
        ypred8=lr.predict(xtest)
        print(ypred8)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A- In GURU TEGH BAHADUR hospital IS")
        hg=(accuracy_score(y8test, ypred8))
        print(hg*100)
        
        clr=RandomForestClassifier(random_state=0)
        clr.fit(xtrain,y9train)
        ypred9=clr.predict(xtest)
        print(ypred9)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP A- In REGIONAL BLOOD TRANFUSION CENTRE CENTRAL ZONE  hospital IS")
        hge=(accuracy_score(y9test, ypred9))
        print(hge*100)
        
        tk.mainloop()
        self.back()
    
    def bne(self, *arg):
        
        traindata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\bneg (1).csv ",delimiter=",")
        testdata=pd.read_csv(r"C:\Users\Aditya Jha(AJ-Adii)\Desktop\Blood\bnegtest.csv",delimiter=",")
        
        df=pd.DataFrame(traindata)
        
        xtrain=df.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtrain.shape
        y1train=df["All India Institute of Medical Sciences (AIIMS)"]
        y1train
        y2train=df["Armed Forces Transfusion Centre"]
        y3train=df["Dr. Ram Manohar Lohia Hospital"]
        y4train=df["E.S.I. Hospital"]
        y5train=df["Safdarjung Hospital"]
        y6train=df["Sucheta Kriplani Hospital"]
        y7train=df["Govind Ballabh Pant Hospital"]
        y8train=df["Guru Tegh Bahadur Hospital"]
        y9train=df["Regional Blood tranfusion Center of Central zone"]
        df2=pd.DataFrame(testdata)
        xtest=df2.drop(['All India Institute of Medical Sciences (AIIMS)','Armed Forces Transfusion Centre','Dr. Ram Manohar Lohia Hospital','E.S.I. Hospital','Safdarjung Hospital','Sucheta Kriplani Hospital','Govind Ballabh Pant Hospital','Guru Tegh Bahadur Hospital','Regional Blood tranfusion Center of Central zone'],axis=1)
        xtest.shape
        y1test=df2["All India Institute of Medical Sciences (AIIMS)"]
        y1test
        y2test=df2["Armed Forces Transfusion Centre"]
        y3test=df2["Dr. Ram Manohar Lohia Hospital"]
        y4test=df2["E.S.I. Hospital"]
        y5test=df2["Safdarjung Hospital"]
        y6test=df2["Sucheta Kriplani Hospital"]
        y7test=df2["Govind Ballabh Pant Hospital"]
        y8test=df2["Guru Tegh Bahadur Hospital"]
        y9test=df2["Regional Blood tranfusion Center of Central zone"]
        cl=RandomForestClassifier(random_state=0)
        cl.fit(xtrain,y1train)
        ypred1=cl.predict(xtest)
        print(ypred1)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP B- In AIIMS IS")
        w=(accuracy_score(y1test, ypred1))
        print(w*100)
        
        c=RandomForestClassifier(random_state=0)
        c.fit(xtrain,y2train)
        ypred2=c.predict(xtest)
        print(ypred2)
        print("THE PERCENTAGE OF FINDING THE BLOOD GROUP B- In ARMED FORCES IS")
        p=(accuracy_score(y2test, ypred2))
        print(p*100)
        
        l=RandomForestClassifier(random_state=0)
        l.fit(xtrain,y3train)
        ypred3=l.predict(xtest)
        print(ypred3)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B- In ram hospital IS")
        q=(accuracy_score(y3test, ypred3))
        print(q*100)

        u=RandomForestClassifier(random_state=0)
        u.fit(xtrain,y4train)
        ypred4=u.predict(xtest)
        print(ypred4)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B- In ESI hospital IS")
        g=(accuracy_score(y4test, ypred4))
        print(g*100)
        
        a=RandomForestClassifier(random_state=0)
        a.fit(xtrain,y5train)
        ypred5=a.predict(xtest)
        print(ypred5)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B- In sarfdung hospital IS")
        h=(accuracy_score(y5test, ypred5))
        print(h*100)
        
        b=RandomForestClassifier(random_state=0)
        b.fit(xtrain,y6train)
        ypred6=b.predict(xtest)
        print(ypred6)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B- In SUCHETA KRIPLANI hospital IS")
        i=(accuracy_score(y6test, ypred6))
        print(i*100)

        y=RandomForestClassifier(random_state=0)
        y.fit(xtrain,y7train)
        ypred7=y.predict(xtest)
        print(ypred7)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B- In GOVIND BALLABH PANT hospital IS")
        j=(accuracy_score(y7test, ypred7))
        print(j*100)
        
        
        lr=RandomForestClassifier(random_state=0)
        lr.fit(xtrain,y8train)
        ypred8=lr.predict(xtest)
        print(ypred8)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B- In GURU TEGH BAHADUR hospital IS")
        hg=(accuracy_score(y8test, ypred8))
        print(hg*100)
        
        clr=RandomForestClassifier(random_state=0)
        clr.fit(xtrain,y9train)
        ypred9=clr.predict(xtest)
        print(ypred9)
        print("THE percentage SCORE OF FINDING THE BLOOD GROUP B- In REGIONAL BLOOD TRANFUSION CENTRE CENTRAL ZONE  hospital IS")
        hge=(accuracy_score(y9test, ypred9))
        print(hge*100)
        


        tk.mainloop()
        self.back()

         
        
        
        
        
       
    def back(self):
        #self.destroy()
        win1()
 
    




app = win1()
app.mainloop()

        
    




