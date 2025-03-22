from tkinter import * #after importing everything, we don't need to write tkinter. before every widget
#it means we dn't need to mention class

#button
def button_clicked():
    new_text = user_input.get()
    my_label.config(text=new_text)


window = Tk()

window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200) #padding

#label
my_label = Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0) #grid() is used to place the widget at the specific location
#grid assumes the whole GUI as a grid and places the widget at the specific location

my_label["text"] = "New Text"
my_label.config(text="New Text") #.config is used to change the properties of the widget

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1) # Use grid instead of pack

#new button
new_button = Button(text="Click", command=button_clicked)
new_button.grid(column=3, row=0) # Use grid instead of pack


#Entry
user_input = Entry(width=10)
user_input.grid(column=2, row=2) # Use grid instead of pack

window.mainloop()
