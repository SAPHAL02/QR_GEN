from tkinter import *
from PIL import ImageTk, Image
import os
login_window = Tk()


login_window.geometry("900x500+200+50")
login_window.title("QR_CODE_GEN | DEVELOPED BY SAPHAL AGARWAL")
login_window.resizable(False, False)

title = Label(login_window, text="  QR_CODE_GEN", font=("times new roman", 40),
                bg="#053246", fg="white", anchor="w").place(x=0, y=0, relwidth=1)



# ====Student frame code========

student_frame = Frame(login_window, bd=2, relief=RIDGE, bg="White")
student_frame.place(x=50, y=100, width=500, height=380)

student_title = Label(student_frame, text="Welcome to the home page", font=(
    "goudy old style", 20), bg="#043256", fg="white").place(x=0, y=0, relwidth=1)



def open_page2():
    os.system('python page2.py')

def open_page3():
    os.system('python page3.py')




# ===Button code===

Button_Gen = Button(student_frame, text="INSERT STUDENT DATA!!!!",font=("times new roman", 18, "bold"),command=open_page2,cursor='hand2', bg="#2196f3", fg="white").place(x=50, y=100, width=380, height=60)



Button_clear = Button(student_frame, text="FETCH STUDENT DATA!!!!", font=("times new roman", 18, "bold"), command=open_page3
                        ,cursor='hand2',bg="#2196f3", fg="white").place(x=50, y=200, width=380, height=60)






# ===msg code=========

msg = ""
lbl_msg = Label(student_frame, text=msg, font=(
    "times new roman", 20), bg="white", fg="green")
lbl_msg.place(x=0, y=310, relwidth=1)

# ====student QR code login_windows========
QR_frame = Frame(login_window, bd=2, relief=RIDGE, bg="White")
QR_frame.place(x=600, y=100, width=250, height=380)



bgImage=ImageTk.PhotoImage(file='insert.jpg')
bgLabel= Label(QR_frame,image=bgImage)
bgLabel.grid()




login_window.mainloop()

