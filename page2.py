from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
import mysql.connector
from tkinter import messagebox


connection = mysql.connector.connect(host='localhost', user='root', password='', port="3307", database='studentdb')
c=connection.cursor()


class QR_Gen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR_CODE_GEN | DEVELOPED BY SAPHAL AGARWAL")
        self.root.resizable(False, False)

        title = Label(self.root, text="  QR_CODE_GEN", font=("times new roman", 40),
                      bg="#053246", fg="white", anchor="w").place(x=0, y=0, relwidth=1)

        # ====Student frame code========
        # ====Variables==============

        self.var_student_name = StringVar()
        self.var_student_ROLL = StringVar()
        self.var_student_Branch = StringVar()
        self.var_student_Year = StringVar()
        self.var_student_College = StringVar()



        student_frame = Frame(self.root, bd=2, relief=RIDGE, bg="White")
        student_frame.place(x=50, y=100, width=500, height=380)

        student_title = Label(student_frame, text="Student Details", font=(
            "goudy old style", 20), bg="#043256", fg="white").place(x=0, y=0, relwidth=1)

        # ==student label===

        label_student_name = Label(student_frame, text="Student Name", font=(
            "times new roman", 15, "bold"), bg="white").place(x=20, y=60)
        label_student_ROLL = Label(student_frame, text="Student ROLL", font=(
            "times new roman", 15, "bold"), bg="white").place(x=20, y=100)
        label_student_Branch = Label(student_frame, text="Student Branch", font=(
            "times new roman", 15, "bold"), bg="white").place(x=20, y=140)
        label_student_Year = Label(student_frame, text="Current Year", font=(
            "times new roman", 15, "bold"), bg="white").place(x=20, y=180)
        label_student_Year = Label(student_frame, text="College", font=(
            "times new roman", 15, "bold"), bg="white").place(x=20, y=220)

        # ===entry box

        txt_ROLL = Entry(student_frame, font=("times new roman", 15),
                        textvariable=self.var_student_name, bg="lightyellow").place(x=200, y=60)
        txt_name = Entry(student_frame, font=("times new roman", 15),
                        textvariable=self.var_student_ROLL, bg="lightyellow").place(x=200, y=100)
        txt_Branch = Entry(student_frame, font=("times new roman", 15),
                        textvariable=self.var_student_Branch, bg="lightyellow").place(x=200, y=140)
        txt_Year = Entry(student_frame, font=("times new roman", 15),
                        textvariable=self.var_student_Year, bg="lightyellow").place(x=200, y=180)
        txt_clg_name = Entry(student_frame, font=("times new roman", 15),
                        textvariable=self.var_student_College, bg="lightyellow").place(x=200, y=220)


        def convertToBinary(filename):
            with open(filename,'rb') as file:
                binarydata=file.read()
            return binarydata


        def insertData():
            S_name= self.var_student_name.get()
            S_roll=  int(self.var_student_ROLL.get())
            S_branch=self.var_student_Branch.get()
            S_curr_year=self.var_student_Year.get()
            S_clg=self.var_student_College.get()
           

           

            insert_query = "INSERT INTO `student_details`(`S_name`, `S_roll`, `S_branch`, `S_curr_year`, `S_clg`,`QR_image`) VALUES (%s,%s,%s,%s,%s,%s)"
            convertpic=convertToBinary("Student_QR/"+str(self.var_student_ROLL.get())+".png")
            vals = (S_name, S_roll, S_branch, S_curr_year, S_clg,convertpic)
            c.execute(insert_query,vals)
            connection.commit()
            
        def exists(self):
            query2='select * from student_details where S_roll=%s'
            c.execute(query2,((self.var_student_ROLL.get(),)))
            row=c.fetchone()

            
            if row!=None:
                messagebox.showerror('Error','User Already exists')


        # ===Button code===

        Button_Gen = Button(student_frame, text="Generate QR", command=lambda: [self.generate(), insertData(),exists()],font=("times new roman", 18, "bold"),cursor='hand2', bg="#2196f3", fg="white").place(x=90, y=270, width=180, height=30)



        Button_clear = Button(student_frame, text="clear", font=("times new roman", 18, "bold"),
                              command=self.clear,cursor='hand2', bg="#607d8b", fg="white").place(x=282, y=270, width=120, height=30)

        # ===msg code=========

        self.msg = ""
        self.lbl_msg = Label(student_frame, text=self.msg, font=(
            "times new roman", 20), bg="white", fg="green")
        self.lbl_msg.place(x=0, y=310, relwidth=1)

        # ====student QR code window========
        QR_frame = Frame(self.root, bd=2, relief=RIDGE, bg="White")
        QR_frame.place(x=600, y=100, width=250, height=380)

        student_title = Label(QR_frame, text="Student QR Code", font=(
            "goudy old style", 20), bg="#043256", fg="white").place(x=0, y=0, relwidth=1)

        # QR main image

        self.qr_code = Label(QR_frame, text="No QR\nAvailable", font=(
            "goudy old style", 15), bg="#3f51b5", fg="white", bd=1, relief=RIDGE)
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def clear(self):
        self.var_student_name.set('')
        self.var_student_ROLL.set('')
        self.var_student_Branch.set('')
        self.var_student_Year.set('')
        self.var_student_College.set('')

        self.msg = ""
        self.lbl_msg.config(text=self.msg)

        self.qr_code.config(image="")

    def generate(self):
        if self.var_student_name.get() == "" or self.var_student_Branch.get() == "" or self.var_student_Year.get() == "" or self.var_student_ROLL.get() == "" or self.var_student_College.get() == "":
            self.msg = "All fields are required with correct input!!!!!"
            self.lbl_msg.config(text=self.msg, fg="red")


        else:
            qr_data=(f" Student ROLL:{self.var_student_ROLL.get()}\n Student Name:{self.var_student_name.get()}\n Student Branch: {self.var_student_Branch.get()}\n Student Year: {self.var_student_Year.get()}\n Student College: {self.var_student_College.get()}")
            self.qr_code_image = qrcode.make(qr_data)

            self.qr_code_image=resizeimage.resize_cover(self.qr_code_image,[180,180])

            
            self.qr_code_image.save("Student_QR/"+str(self.var_student_ROLL.get())+".png")
            #===QR code Image update===

            self.im=ImageTk.PhotoImage(self.qr_code_image)
            self.qr_code.config(image=self.im)
            #==code for updating===
            self.msg = "QR Generated successfully!!!!!"
            self.lbl_msg.config(text=self.msg, fg="green")
           


root = Tk()
object = QR_Gen(root)
root.mainloop()

