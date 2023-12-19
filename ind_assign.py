import tkinter
from tkinter import ttk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="taekwondo_registration"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

def collect_data():
    Name= Member_Name_entry.get()
    ID = int (Member_ID_entry.get())
    Gender = Member_Gender_combobox.get()
    YoB= int(Member_YoB_entry.get())

    # Calculate the age. This will be derived from your selection (Year of birth).
    Age = 2023 - YoB

    # To insert your Data to your database, As for this example, you have 5 attributes. (4 Attributes from your selection (Name, ID Number, Gender, Year of born) and another attributes that derived from your attributes (age))
    sql = "INSERT INTO Member_Information (Name, ID_Number, Gender, Year_of_Born, Age) VALUES (%s, %s, %s, %s, %s)"
    val = (Name, ID, Gender, YoB, Age)
    mycursor.execute(sql, val)
    mydb.commit()

    # To Print back The output. It will happen in the function collect_data(). The f before the string indicates an f-string in Python. 
    output_label.config(text=f"Name: {Name}, ID_Number:{ID}, Gender: {Gender}, Year of born: {YoB}, Age: {Age}")

# Your Main window, You need to have the title, geometry (MUST)
root = tkinter.Tk()
root.title("Registration Form")
frame = tkinter.Frame(root)
frame.pack()

# Page Title
Label1 = ttk.Label(root, text= "Taekwondo Registration Form", font=("Cooper Black", 25))
Label1.pack(anchor= "n", padx= 55)

#Member info
Member_Info =tkinter.LabelFrame(frame, text="Member Information")
Member_Info.grid(row= 0, column= 0, padx= 20, pady=10)

Member_Name_label = tkinter.Label(Member_Info, text="Name")
Member_Name_label.grid(row= 0, column=0)
Member_Name_entry = tkinter.Entry(Member_Info)
Member_Name_entry.grid(row= 0, column= 1)

Member_ID_label = tkinter.Label(Member_Info, text="ID Number")
Member_ID_label.grid(row= 1, column= 0)
Member_ID_entry = tkinter.Entry(Member_Info)
Member_ID_entry.grid(row= 1, column= 1)

Member_Gender_label= tkinter.Label(Member_Info, text="Gender")
Member_Gender_combobox = ttk.Combobox(Member_Info, values=["Male", "Female"])
Member_Gender_label.grid(row=1, column=2)
Member_Gender_combobox.grid(row= 2, column= 2)

Member_YoB_label = tkinter.Label(Member_Info, text="Year of Birth")
Member_YoB_label.grid(row= 2, column= 0)
Member_YoB_entry = tkinter.Entry(Member_Info)
Member_YoB_entry.grid(row= 2, column= 1) 

for widget in Member_Info.winfo_children():
    widget.grid_configure(padx= 10, pady= 5)

# Button
button = tkinter.Button(frame, text="Submit", command= collect_data)
button.grid(row= 3, column= 0, sticky="news", padx= 20, pady= 10)

# Output Label & result
label = ttk.Label(root, text='Member Information', font=("Cooper black",11))
label.pack(ipadx=10, ipady=10)
output_label = ttk.Label(root, text="")
output_label.pack()


root.mainloop()