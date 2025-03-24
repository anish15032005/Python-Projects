from tkinter import *
import math
import winsound  # Import winsound for Windows beep sound
import os  # Alternative for Linux/macOS

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)  # Cancel the current timer
    canvas.itemconfig(timer_text, text="00:00")  # Reset the timer text
    title_label.config(text="Timer", fg=GREEN)  # Reset the title label
    check_mark.config(text="")  # Clear the check marks
    reps = 0  # Reset the repetition counter

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1  # Increment the repetition counter
    
    work_sec = WORK_MIN * 60  # Convert work minutes to seconds
    short_break_sec = SHORT_BREAK_MIN * 60  # Convert short break minutes to seconds
    long_break_sec = LONG_BREAK_MIN * 60  # Convert long break minutes to seconds

    if reps % 8 == 0:
        count_down(long_break_sec)  # Start long break
        title_label.config(text="Break", fg=RED)  # Update title label for long break
    elif reps % 2 == 0:
        count_down(short_break_sec)  # Start short break
        title_label.config(text="Break", fg=PINK)  # Update title label for short break
    else:
        count_down(work_sec)  # Start work session
        title_label.config(text="Work", fg=GREEN)  # Update title label for work session

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)  # Calculate minutes
    count_sec = count % 60  # Calculate seconds
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Add leading zero to seconds if less than 10
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # Update timer text
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # Call count_down after 1 second
    else:
        play_beep()  # Beep sound when cycle completes
        start_timer()  # Start the next timer cycle
        marks = ""
        work_sessions = math.floor(reps / 2)  # Calculate number of work sessions completed
        for _ in range(work_sessions):
            marks += "✓"  # Add a check mark for each work session
        check_mark.config(text=marks)  # Update check marks

# ---------------------------- BEEP SOUND FUNCTION ------------------------------- #
def play_beep():
    try:
        winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500ms (Windows)
    except:
        os.system('play -nq -t alsa synth 0.5 sine 1000')  # Alternative for macOS/Linux

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Canvas setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # Load tomato image
canvas.create_image(100, 112, image=tomato_img)  # Display tomato image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check marks
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_mark.grid(column=1, row=3)

window.mainloop()
