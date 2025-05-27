from tkinter import * 
import pandas as pd 
import random
current_card = {}
to_learn = {}


BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')  # Convert DataFrame to a list of dictionaries
else:
    to_learn = data.to_dict(orient='records')
# print(to_learn)
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)  # Cancel the previous timer if it exists
    current_card =  random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)  # Save the new timer id
    
    
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    
def is_known():
    to_learn.remove(current_card)  # Remove the known word from the list
    # print(len(to_learn))  # Print the number of words left to learn
    data = pd.DataFrame(to_learn)  # Convert the updated list back to a DataFrame
    data.to_csv("data/words_to_learn.csv", index=False)  # Save the updated list to a CSV file
    next_card()  # Show the next card
    
    
    
    
    


window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

flip_timer  = window.after(3000,func=flip_card)


canvas = Canvas(width = 800, height = 526)
card_front_img = PhotoImage(file = "images/card_front.png")
card_back_img = PhotoImage(file = "images/card_back.png")
card_background = canvas.create_image(400, 263, image = card_front_img)
card_title = canvas.create_text(400,150,text="",font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263,text="",font=("Ariel", 60, "bold"))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas.grid(row =0, column = 0, columnspan=2) 

cross_image = PhotoImage(file = "images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command = next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file = "images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command = is_known)
known_button.grid(row=1, column=1)


next_card()  # Show the first card when the program starts

window.mainloop()