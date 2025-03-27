from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    # Check if any field is empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # Ask for confirmation before saving the password
        is_ok = messagebox.askokcancel(
            title=website, 
            message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?"
        )
        
        # Save the data only if the user clicks "OK"
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                # Clear the input fields after saving
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Create the main application window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)  # Add padding around the window
window.minsize(width=200, height=200)  # Set a minimum size for the window

# Add a canvas to display the logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")  # Load the logo image
canvas.create_image(100, 100, image=logo_img)  # Place the image at the center of the canvas
canvas.grid(row=0, column=1)  # Use grid layout for positioning

# Labels
website_label = Label(text="Website:")  # Label for the website field
website_label.grid(row=1, column=0)  # Position the label in the grid
email_label = Label(text="Email/Username:")  # Label for the email/username field
email_label.grid(row=2, column=0)  # Position the label in the grid
password_label = Label(text="Password:")  # Label for the password field
password_label.grid(row=3, column=0)  # Position the label in the grid

# Entries
website_entry = Entry(width=35)  # Entry field for the website
website_entry.grid(row=1, column=1, columnspan=2)  # Span across two columns for better alignment
website_entry.focus()  # Set focus on the website entry field by default
email_entry = Entry(width=35)  # Entry field for the email/username
email_entry.grid(row=2, column=1, columnspan=2)  # Span across two columns for better alignment
email_entry.insert(0,"anish2211@gmail.com")  # Pre-fill the email/username field
password_entry = Entry(width=21)  # Entry field for the password
password_entry.grid(row=3, column=1)  # Position the entry field next to the password label

# Buttons
generate_password_button = Button(text="Generate Password",command=generate_password)  # Button to generate a password
generate_password_button.grid(row=3, column=2)  # Position the button next to the password entry field
add_button = Button(text="Add", width=36,command=save_password)  # Button to add/save the password
add_button.grid(row=4, column=1, columnspan=2)  # Span across two columns for better alignment

# Start the Tkinter event loop
window.mainloop()