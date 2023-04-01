from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
import mysql.connector
login_window=Tk()
from tkinter import messagebox

connection = mysql.connector.connect(host='localhost', user='root', password='', port="3307", database='studentdb')
c=connection.cursor()


# FUNCTIONALITY PART


def on_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
def onpass_enter(event):    
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def hide():
    closeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=show)

def show():
    closeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    
    eyeButton.config(command=hide)


def sign_up():
    login_window.destroy()
    import signup


def login_user():
    if  usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')

    else:
        try:
            connection = mysql.connector.connect(host='localhost', user='root', password='', port="3307", database='studentdb')
            mycursor=connection.cursor()

        except:
            messagebox.showerror('Error','Database Connectivity Issue,Please Try Again')
            return

        
        query='select * from authdata where username=%s and password=%s'
        mycursor.execute(query,((usernameEntry.get(),passwordEntry.get())))

        row= mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username and password')
        
        else:
            messagebox.showinfo('Success','Login is successful')
            login_window.destroy()
            import page1


def forget_pass():
    def change_pass():
        if  change_user.get()=='' or pass_entry.get()=='' or confirm_pass_entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=window)


        elif pass_entry.get() != confirm_pass_entry.get():
            messagebox.showerror('Error','Password and confirm password are not matching',parent=window)

        else:
            connection = mysql.connector.connect(host='localhost', user='root', password='', port="3307", database='studentdb')
            mycursor=connection.cursor()

            query = 'select * from authdata where username=%s'
            mycursor.execute(query,(change_user.get(),))
            row=mycursor.fetchall()

            if len(row) == 0:
                messagebox.showerror('Error','Incorrect username',parent=window)
            else:
                query = 'update authdata set password=%s where username=%s'
                mycursor.execute(query,((confirm_pass_entry.get(),change_user.get(),)))
                connection.commit()
                connection.close()
                messagebox.showinfo('Success','Password is reset, please login with new password',parent=window)
                window.destroy()

    window=Toplevel()
    window.title('Change Password')
    window.resizable(False, False)

    bgpic=ImageTk.PhotoImage(file='pass_img.jpg')
    bgLabel= Label(window,image=bgpic)
    bgLabel.grid()


    heading_rst =Label(window,text="RESET PASSWORD", font=('arial',18,'bold'),bg='white',fg='magenta2')
    heading_rst.place(x=480,y=60)


    userlabel = Label(window,text='Username', font=("arial", 12,'bold'),bg='white',fg='orchid1')
    userlabel.place(x=470, y=130)

    change_user = Entry(window,width=25,fg='magenta2', font=('arial',11,'bold'),bd=0)
    change_user.place(x=470,y=160)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=180)



    passlabel = Label(window,text='New Password', font=("arial", 12,'bold'),bg='white',fg='orchid1')
    passlabel.place(x=470, y=210)

    
    pass_entry = Entry(window,width=25,fg='magenta2', font=('arial',11,'bold'),bd=0)
    pass_entry.place(x=470,y=240)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=260)


    confirm_pass_label = Label(window,text='Confirm Password', font=("arial", 12,'bold'),bg='white',fg='orchid1')
    confirm_pass_label.place(x=470, y=290)

    
    confirm_pass_entry = Entry(window,width=25,fg='magenta2', font=('arial',11,'bold'),bd=0)
    confirm_pass_entry.place(x=470,y=320)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=340)

    
    Submit_Button=Button(window,text='Submit',command=change_pass,font=('Open Sans',16,'bold'),fg='white',bg='magenta2',activeforeground='white',activebackground='magenta2',cursor='hand2',bd=0,width=19)
    Submit_Button.place(x=470,y=390)




    window.mainloop()

# GUI PART

login_window.geometry("900x500+200+50")
login_window.title("QR_CODE_GEN | DEVELOPED BY SAPHAL AGARWAL")
login_window.resizable(False, False)

    


bgImage=ImageTk.PhotoImage(file='log_img.jpg')
bgLabel= Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)



heading =Label(login_window,text="USER LOGIN", font=('times new roman',16,'bold'),bg='white',fg='firebrick1')
heading.place(x=570,y=100)



# username and password
usernameEntry = Entry(login_window, font=("times new roman", 15),bd=0,fg='firebrick1')
usernameEntry.place(x=540, y=160)

passwordEntry = Entry(login_window, font=("times new roman", 15),bd=0,fg='firebrick1',show="*")
passwordEntry.place(x=540, y=210)

usernameEntry.insert(0,'Username')
passwordEntry.insert(0,'Password')

usernameEntry.bind('<FocusIn>',on_enter)
passwordEntry.bind('<FocusIn>',onpass_enter)


Frame(login_window,width=200,height=2,bg='firebrick1').place(x=540,y=183)
Frame(login_window,width=200,height=2,bg='firebrick1').place(x=540,y=235)



closeye= PhotoImage(file='closeye.png')
eyeButton=Button(login_window,image=closeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=718,y=206)


forgotButton=Button(login_window,text='Forgot Password?',command=forget_pass,bd=0,bg='white',font=('times new roman',11,'bold'),fg='firebrick1',activeforeground='firebrick1',activebackground='white',cursor='hand2')
forgotButton.place(x=619,y=245)


loginButton=Button(login_window,text='Login',command=login_user,font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=17)
loginButton.place(x=524,y=300)



signupLabel = Label(login_window,text='Don`t have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=524,y=360)


New_acc_Button=Button(login_window,text='Create new one',command=sign_up,font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,width=13)
New_acc_Button.place(x=657,y=359)



login_window.mainloop()