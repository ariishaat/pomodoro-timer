# pomodoro timer using python GUI

from tkinter import *
import time
import math

## global variables
brown = "#9C6644"
red = "#C82119"
green = "#1F5C2E"
black = "#000000"
font = "Courier"
work = 25
shortBreak = 5
longBreak = 15
repeats = 0
timer = None


tk=Tk()
tk.title('Pomodoro Timer') ## window title

tk.minsize(300, 200)

def responsive_bg(event):
    '''
    Function to make the background colour responsive 
    to different screen sizes
    '''
    tk.configure(bg=brown)

tk.configure(bg=brown)
tk.bind('<Configure>', responsive_bg) # Bind resizing event

canvas = Canvas(width=500, height=100, bg=brown, highlightthickness=0)
canvas.pack()

header_frame = Frame(tk,bg=brown)
header_frame.pack(fill='x',side="top")

timer_text = canvas.create_text(250,50, text="00:00", fill=None, font=(font, 30, "bold"), anchor="center")

def update_timer_text(event):
    width = event.width
    height = event.height
    font_size = min(width // 12, height // 6)
    canvas.itemconfig(timer_text, font=(font, 30, "bold"))


tk.bind('<Configure>', update_timer_text)

title = Label(text="Timer", fg=black, bg=brown, font=(font, 50))
title.pack(fill='x')

# ----------------------------------------------------------------- #
def reset():
    tk.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    global reps
    reps = 0

def starter():
    global repeats
    repeats += 1
    working_sec = work * 60
    shortBS = shortBreak * 60
    longBS = longBreak * 60

    if repeats % 8 == 0: ## every 8th rep = long break
        counting(longBS)
        title.config(text="Long Break",fg=red)
    elif repeats % 2 == 0:
        counting(shortBS)
        title.config(text="Short Break", fg=red)
    else:
        counting(working_sec)
        title.config(text="Work", fg=green)

# ----------------------------------------------------------------- #

button_frame = Frame(tk, bg=brown)
button_frame.pack(fill='x')

start_button = Button(button_frame, text="Start", highlightthickness=0, command=starter)
start_button.configure(bg=brown, highlightbackground=brown)
start_button.pack(side=LEFT, padx=5, pady=10)

reset_button = Button(button_frame, text="Reset", highlightthickness=0, command=reset)
reset_button.configure(bg=brown, highlightbackground=brown)
reset_button.pack(side=RIGHT, padx=5, pady=10)

# ----------------------------------------------------------------- #

def counting(count):
    #timer countdown using recursion
    minutes = math.floor (count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"
        canvas.itemconfig
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    
    if count > 0:
        global timer
        timer = tk.after(1000,counting, count - 1)
    else:
        starter()
        work = math.floor(repeats/2)


tk.mainloop()

# press reset to end the timer