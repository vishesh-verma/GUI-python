from Tkinter import *
import sqlite3

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (name1.get(), reg_no1.get()))
def show():
    Label(master, text=name1.get()).grid(row=5,column=1)
    Label(master, text=reg_no1.get()).grid(row=6,column=1)
def data():
      conn = sqlite3.connect("first.db")
      c = conn.cursor()

      def create_table():
          c.execute('CREATE TABLE IF NOT EXISTS student(name TEXT, reg_no REAL)')
      def data_entry():

           name=name1.get()
           reg_no=reg_no1.get()
           c.execute("INSERT INTO student (name, reg_no) VALUES (?,?)",
                 (name, reg_no))
           conn.commit()



      create_table()
      data_entry()
      c.close
      conn.close()
def retrive():
    conn = sqlite3.connect("first.db")
    cursor= conn.execute("SELECT name,reg_no from student")
    a=8
    for row in cursor:
       Label(master, text="name :").grid(row=a,column=1)
       Label(master, text="registration no: ").grid(row=a+1,column=1)
       Label(master, text=row[0]).grid(row=a,column=2)
       Label(master, text=row[1]).grid(row=a+1,column=2)
       a=a+2
    conn.close()

master = Tk()

Label(master, text="name").grid(row=0)
Label(master, text="reg").grid(row=1)

name1 = Entry(master)
reg_no1 = Entry(master)

name1.grid(row=0, column=1)
reg_no1.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Show', command=show).grid(row=3, column=2, sticky=W, pady=4)
Button(master, text='Enter', command=data).grid(row=3, column=4, sticky=W, pady=4)
Button(master, text='retrive data', command=retrive).grid(row=7, column=4, sticky=W, pady=4)


mainloop( )
