from tkinter import *

# Function to calculate miles to kilometers
def calculate():
    miles = float(user_input.get())  # Get the value from the entry widget
    km = round(miles * 1.609)  # Convert miles to kilometers
    label3.config(text=f"{km}")  # Update the label with the result

# Create the main window
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)  # Add padding around the window
window.minsize(width=300, height=100)  # Set minimum size of the window

# Entry widget to input miles
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

# Label for "Miles"
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

# Label for "is equal to"
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

# Label to display the result in kilometers
label3 = Label(text="0")
label3.grid(column=1, row=1)

# Label for "Km"
label4 = Label(text="Km")
label4.grid(column=2, row=1)

# Button to trigger the calculation
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# Start the main event loop
window.mainloop()


