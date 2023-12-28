import tkinter as tk
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

# Function to calculate the total amount
def calculate_total_amount():
    # For simplicity, let's assume a fixed registration fee of RM50
    registration_fee = 50
    return registration_fee

def collect_data():
    Name= Member_Name_entry.get()
    ID = int (Member_ID_entry.get())
    Gender = Member_Gender_var.get()
    YoB= int(Member_YoB_entry.get()) 

    # Calculate the age. This will be derived from your selection (Year of birth).
    Age = 2023 - YoB

    # Apply a 10% discount for kids between 5 to 12 years old
    if Age >= 5 and Age <= 12:
        discount_percentage = 10  # 10% discount
        eligibility_message = "You are eligible to get a {}% discount!".format(discount_percentage)
    else:
        discount_percentage = 0  # No discount
        eligibility_message = "You are not eligible to get a discount."

    # Calculate the total amount 
    total_amount = calculate_total_amount()

    # Calculate the discounted amount directly using the percentage value
    discounted_amount = total_amount - (total_amount * (discount_percentage / 100))

    # To insert your Data to your database, As for this example, you have 6 attributes. (4 Attributes from your selection (Name, ID Number, Gender, Year of born) and 2 attributes that derived from your attributes (age and discount))
    sql = "INSERT INTO Member_Information (Name, ID_Number, Gender, Year_of_Born, Age, Discount, Total_Amount) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Name, ID, Gender, YoB, Age, discount_percentage, discounted_amount)
    mycursor.execute(sql, val)
    mydb.commit()

    # To Print back The output. It will happen in the function collect_data(). The f before the string indicates an f-string in Python. 
    output_label.config(text=f"{eligibility_message}\n\n"
    f"Name: {Name}, ID Number: {ID}, Gender: {Gender}\n"
    f"Year of Born: {YoB}, Age: {Age}, Discount: {discount_percentage}%, Total Amount: RM {discounted_amount}\n\n"
    f"THANK YOU")

# Your Main window, You need to have the title, geometry (MUST)
root = tk.Tk()
root.title("Registration Form")
frame = tk.Frame(root)
frame.grid(row=0, column=0)


# Page Title
Label1 = tk.Label(root, text= "Taekwondo Registration Form", font=("Impact", 20), bg= "lightseagreen")
Label1.grid(row= 0, column= 0, sticky= "n", padx= 55)

#Member info
Member_Info =tk.LabelFrame(root, text="Member Information", font=("Impact", 10))
Member_Info.grid(row= 1, column= 0, padx= 20, pady=10)

Member_Name_label = tk.Label(Member_Info, text="Name")
Member_Name_label.grid(row= 1, column=0)
Member_Name_entry = tk.Entry(Member_Info)
Member_Name_entry.grid(row= 1, column= 1)

Member_ID_label = tk.Label(Member_Info, text="ID Number")
Member_ID_label.grid(row= 2, column= 0)
Member_ID_entry = tk.Entry(Member_Info)
Member_ID_entry.grid(row= 2, column= 1)

# Gender Dropdown (Label)
Gender_label = tk.Label(Member_Info, text="Gender")
Gender_label.grid(row= 2, column= 2)

# Trip Type Dropdown
Member_Gender_var = tk.StringVar(Member_Info)
Member_Gender_var.set("Choose your Gender")  # Default value before your selection
Member_Gender_dropdown = tk.OptionMenu(Member_Info, Member_Gender_var, "Male", "Female")
Member_Gender_dropdown.grid(row= 3, column= 2, pady=10)

Member_YoB_label = tk.Label(Member_Info, text="Year of Birth")
Member_YoB_label.grid(row= 3, column= 0)
Member_YoB_entry = tk.Entry(Member_Info)
Member_YoB_entry.grid(row= 3, column= 1) 

for widget in Member_Info.winfo_children():
    widget.grid_configure(padx= 10, pady= 5)

# Only to inform those who fill out this form
information_text = tk.Text(root, height=3, width=49)
information_text.grid(row= 4, column= 0)
information_text.insert(tk.END, "Registration Fee : RM 50 \n\n")
information_text.insert(tk.END, "Discount for kids between 5 to 12 years old ONLY")

# Button
button = tk.Button(root, text="Submit", command= collect_data, bg= "lightseagreen")
button.grid(row= 5, column= 0, sticky="news", padx= 20, pady= 10)

# Output Label & result
label = tk.Label(root, text='Member Information', font=("Impact",13))
label.grid(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.grid()


root.mainloop()