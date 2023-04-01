from tkinter import *
from tkinter import filedialog
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
from io import BytesIO
import mysql.connector
from tkinter import messagebox

connection = mysql.connector.connect(host='localhost', user='root', password='', port="3307", database='studentdb')
mycursor =connection.cursor()


class QR_Gen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR_CODE_GEN | DEVELOPED BY SAPHAL AGARWAL")
        self.root.resizable(False, False)

        title = Label(self.root, text="  QR_CODE_GEN", font=("times new roman", 40),
                      bg="#053246", fg="white", anchor="w").place(x=0, y=0, relwidth=1)

        # ====Student frame code========
        # ====Variable==============

        
        self.var_student_ROLL = StringVar()
        



        student_frame = Frame(self.root, bd=2, relief=RIDGE, bg="White")
        student_frame.place(x=50, y=100, width=500, height=380)

        student_title = Label(student_frame, text="Student Details", font=(
            "goudy old style", 20), bg="#043256", fg="white").place(x=0, y=0, relwidth=1)

        # ==student label===

        
        label_student_ROLL = Label(student_frame, text="Enter Roll No", font=(
            "times new roman", 15, "bold"), bg="white").place(x=90, y=120)
       
        # ===entry box

        
        txt_ROLL = Entry(student_frame, font=("times new roman", 15),
                        textvariable=self.var_student_ROLL, bg="lightyellow").place(x=93, y=160)
       

        
        def fetch_image():
            # retrieve roll number entered by user
            roll_num = (self.var_student_ROLL.get())
           

            # query to retrieve blob image data for student with specified roll number
            mycursor.execute("SELECT QR_image FROM `student_details` WHERE S_roll = %s", (roll_num,))
            self.result = mycursor.fetchone()

            # create PhotoImage object from blob data and display in label widget
            if self.result is not None:
                image = Image.open(BytesIO(self.result[0]))
                self.im=ImageTk.PhotoImage(image)
                self.image_label.config(image=self.im) 
            
            else:
                self.clear()
                messagebox.showinfo("Error", "No image found for the entered roll number.")



        # ===Button code===

        Button_fet = Button(student_frame, text="Fetch image", command=fetch_image,font=("times new roman", 18, "bold"), bg="#2196f3", fg="white").place(x=92, y=230, width=180, height=30)



        Button_clear = Button(student_frame, text="clear", font=("times new roman", 18, "bold"),
                              command=self.clear, bg="#607d8b", fg="white").place(x=284, y=230, width=120, height=30)

        
        



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

        self.image_label = Label(QR_frame, text="No QR\nAvailable", font=(
            "goudy old style", 15), bg="#3f51b5", fg="white", bd=1, relief=RIDGE)
        self.image_label.place(x=35, y=100, width=180, height=180)



        def save_file():
            roll_number = self.var_student_ROLL.get()
            file_name = f"{roll_number}.jpg"
            fob = filedialog.asksaveasfile(defaultextension='.jpg', initialfile=file_name, 
                                        filetypes=[(('JPEG', '*.jpg'), ('All Files', '*.*'))])
            
            if fob is not None:
                # Open the file and write the image data to it
                with open(fob.name, 'wb') as file:
                    file.write(self.result[0])


        Button_save = Button(QR_frame, text="Save Image",command=save_file,font=("times new roman", 18,),
                    bg="#2196f3", fg="white").place(x=65, y=300,width=120, height=30)




    def clear(self):
        self.var_student_ROLL.set('')
        

        self.msg = ""
        self.lbl_msg.config(text=self.msg)

        self.image_label.config(image="")
        

   
root = Tk()
object = QR_Gen(root)
root.mainloop()

