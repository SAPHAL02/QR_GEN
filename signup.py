from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
import mysql.connector
from tkinter import messagebox


signup_window=Tk()





#func

def login_page():
    signup_window.destroy()
    import Login


def clear():
    emailEntry.delete(0,END)
    UsernameEntry.delete(0,END)
    PasswordEntry.delete(0,END)
    ConfirmPasswordEntry.delete(0,END)


def connect_database():
    if emailEntry.get()=='' or UsernameEntry.get()=='' or PasswordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')

    elif PasswordEntry.get() != ConfirmPasswordEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    
    else:
        try:
            connection = mysql.connector.connect(host='localhost', user='root', password='', port="3307", database='studentdb')
            mycursor=connection.cursor()

        except:
            messagebox.showerror('Error','Database Connectivity Issue,Please Try Again')
            return


        query1='select * from authdata where email=%s'
        mycursor.execute(query1,(emailEntry.get(),))
        roww= mycursor.fetchone()

        
        query2='select * from authdata where username=%s'
        mycursor.execute(query2,(UsernameEntry.get(),))
        row=mycursor.fetchone()

        
        if row!=None or roww!=None:
            messagebox.showerror('Error','User Already exists')
    
        else:
            query2="insert into authdata(email,username,password) values(%s,%s,%s)"
            mycursor.execute(query2,((emailEntry.get(),UsernameEntry.get(),PasswordEntry.get())))
            connection.commit()
            connection.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            signup_window.destroy()
            import Login





# GUI PART

signup_window.geometry("900x500+120+50")
signup_window.title("QR_CODE_GEN | DEVELOPED BY SAPHAL AGARWAL")
signup_window.resizable(False, False)

    


bgImage=ImageTk.PhotoImage(file='sign_img.jpg')
bgLabel= Label(signup_window,image=bgImage)
bgLabel.grid()

frame= Frame(signup_window,bg='white')
frame.place(x=530,y=65)

heading =Label(frame,text="CREATE AN ACCOUNT", font=('times new roman',15,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=15,pady=15)


emaillabel=Label(frame,text='Email',font=('times new roman',15,'bold'),bg='white',fg='firebrick1')
emaillabel.grid(row=1,column=0,sticky='w',padx=25)

emailEntry=Entry(frame,width=24,font=('times new roman',15,'bold'),bg='white',fg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)



Usernamelabel=Label(frame,text='Username',font=('times new roman',15,'bold'),bg='white',fg='firebrick1')
Usernamelabel.grid(row=3,column=0,sticky='w',padx=25)

UsernameEntry=Entry(frame,width=24,font=('times new roman',15,'bold'),bg='white',fg='firebrick1')
UsernameEntry.grid(row=4,column=0,sticky='w',padx=25)



Passwordlabel=Label(frame,text='Password',font=('times new roman',15,'bold'),bg='white',fg='firebrick1')
Passwordlabel.grid(row=5,column=0,sticky='w',padx=25)

PasswordEntry=Entry(frame,width=24,font=('times new roman',15,'bold'),bg='white',fg='firebrick1')
PasswordEntry.grid(row=6,column=0,sticky='w',padx=25)



ConfirmPasswordlabel=Label(frame,text='Confirm Password',font=('times new roman',15,'bold'),bg='white',fg='firebrick1')
ConfirmPasswordlabel.grid(row=7,column=0,sticky='w',padx=25)

ConfirmPasswordEntry=Entry(frame,width=24,font=('times new roman',15,'bold'),bg='white',fg='firebrick1')
ConfirmPasswordEntry.grid(row=8,column=0,sticky='w',padx=25)


signupButton=Button(frame,text='Signup',command=connect_database,font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=17)
signupButton.grid(row=9,column=0,pady=10)



loginLabel = Label(frame,text='Already have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
loginLabel.grid(row=10,column=0)


loginButton=Button(frame,text='Log in',command=login_page,font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,width=15)
loginButton.grid(row=11,column=0)



signup_window.mainloop()