# pomodoro timer using python GUI

from tkinter import *
import time
import math

## global variables
pink = "#FAD8D6"
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
tk.title('Pomodoro') #window title

canvas = Canvas(width=500, height=100, bg=pink, highlightthickness=0)
canvas.pack()

header_frame = Frame(tk,bg=pink)
header_frame.pack(fill='x',side="top")
header_label = Label(header_frame, text="Pomodoro Timer", font=("Helvetica", 16), fg=black, bg=pink)
header_label.pack() ## need to fix header to appear at top

timer_text = canvas.create_text(250,50, text="00:00", fill=black, font=(font, 30, "bold"), anchor="center")

title = Label(text="Timer", fg=black, bg=pink, font=(font, 50))
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

button_frame = Frame(tk, bg=pink)
button_frame.pack(fill='x') #need to fix this, fill should be pink

start_button = Button(text="Start", highlightthickness=0, command=starter)
start_button.configure(bg=pink, highlightbackground=pink)
start_button.pack(side="right")

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.configure(bg=pink, highlightbackground=pink)
reset_button.pack(side="left")

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