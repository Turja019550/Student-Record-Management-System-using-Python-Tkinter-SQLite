import sqlite3
from tkinter import *

root = Tk()
root.geometry('500x700')
root.title("Python_56_TURJA")

def recordshow():
    con = sqlite3.connect("my database.db")
    Cursor = con.cursor()
    Cursor.execute("SELECT * FROM Student")
    records = Cursor.fetchall()
    print_record = ""
    for records in records:
        print_record += str(records[0]) + " " + str(records[1]) + " " + str(records[2]) + "\n"

        lblrecordshow = Label(text=print_record)
        lblrecordshow.grid(row=130, column=0, columnspan=2)
    con.close()

def recordDelete():
    con = sqlite3.connect("my database.db")
    Cursor = con.cursor()
    Cursor.execute("DELETE FROM Student WHERE id =" + txtID.get())
    con.commit()
    message = "Record Deleted Succesfully!!!!!!!"
    con.close()
    txtID.delete(0, END)

    lblMessageShow = Label(text=message)
    lblMessageShow.grid(row=121, column=0, columnspan=2)
    recordshow() 

def recordSave():
    con = sqlite3.connect("my database.db")
    Cursor = con.cursor()
    Cursor.execute("INSERT INTO Student (Name, Email) VALUES (:txt_name,:txt_email)",
                          {
                            'txt_name':txtname.get(),
                            'txt_email':txtEmail.get()        
                        })
    con.commit()
    print("Record Save Successfully!!!!")
    con.close()

    txtname.delete(0, END)
    txtEmail.delete(0, END)

def editRecord():
    global editor
    global txtname_edit
    global txtEmail_edit 
    editor = Tk()
    editor.geometry('400x400')
    editor.title("Edit Record")

    lblspace101 = Label(editor)
    lblspace101.grid(row=0, column=0)

    lblspace102 = Label(editor)
    lblspace102.grid(row=1, column=0)

    lblName_edit = Label(editor, text=("Student Name"))
    lblName_edit.grid(row=10, column=0)
    txtname_edit = Entry(editor, width=50)
    txtname_edit.grid(row=10, column=1)

    lblEmail_edit = Label(editor, text=("Student Email"))
    lblEmail_edit.grid(row=11, column=0)
    txtEmail_edit = Entry(editor, width=50)
    txtEmail_edit.grid(row=11, column=1)

    con = sqlite3.connect("my database.db")
    Cursor = con.cursor()
    Cursor.execute("SELECT * FROM Student WHERE id =" + txtID.get())
    record = Cursor.fetchall()
    for data in record:
        txtname_edit.insert(0, data[1])
        txtEmail_edit.insert(0, data[2])

    btnupdate = Button(editor, text="update", command=recordUpdate)
    btnupdate.grid(row=110, column=0)
    con.close()

def recordUpdate():
    con = sqlite3.connect("my database.db")
    Cursor = con.cursor()
    Cursor.execute("""
                    UPDATE Student SET 
                    Name = :name,
                    Email = :email
                    WHERE id = :id""",
                    {'name':txtname_edit.get(),
                     'email':txtEmail_edit.get(),
                     'id': txtID.get()
                    }
                    )

    con.commit()
    con.close()  
    editor.destroy()

lblspace01 = Label(root)
lblspace01.grid(row=0, column=1)

lblspace02 = Label(root)
lblspace02.grid(row=1, column=0)

lblName = Label(root, text=("Student Name"))
lblName.grid(row=10, column=0)
txtname = Entry(root, width=50)
txtname.grid(row=10, column=1)

lblEmail = Label(root, text=("Student Email"))
lblEmail.grid(row=11, column=0)
txtEmail = Entry(root, width=50)
txtEmail.grid(row=11, column=1)

lblspace101 = Label(root)
lblspace101.grid(row=102, column=0)

lblID = Label(root, text=("Edit/Delete"))
lblID.grid(row=102, column=0)
txtID = Entry(root, width=50)
txtID.grid(row=102, column=1)

lblspace103 = Label(root)
lblspace103.grid(row=103, column=0)

btnsave = Button(root, text="Save", command=recordSave)
btnsave.grid(row=110, column=0)

btnedit = Button(root, text="Edit", command=editRecord)
btnedit.grid(row=110, column=1)

btnshow = Button(root, text="show", command=recordshow) 
btnshow.grid(row=111, column=0)

btndelete = Button(root, text="delete", command=recordDelete)
btndelete.grid(row=111, column=1)

lblspace201 = Label(root)
lblspace201.grid(row=120, column=0)

root.mainloop()
