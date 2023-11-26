from tkinter import *
import time
import math

## global style variables
brown = "#9C6644"
red = "#C82119"
green = "#1F5C2E"
black = "#000000"
font = "Courier"


tk=Tk()
tk.title('Pomodoro Timer') ## window title

tk.minsize(300, 200) ## window should not minimize less than this size

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

title = Label(text="Timer", fg=black, bg=brown, font=(font, 50))
title.pack(fill='x')

# -------------- timer functions --------------------------------- #

##global function vars
timer = None
running = False ## tracking timer movement
current_time = 0

work = 25
shortBreak = 5
longBreak = 15
repeats = 0

def reset():
    '''
    Function for reset button: resets timer
    '''
    global running
    tk.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=black)
    running = False
    current_time = 0

def start_timer(duration, label_text, label_color):
    '''
    configures start timer, if start timer is pressed the second time,
    it will start on the next part of the cycle, (technically not supposed to happen,
    adding this for now to fix the issue of when start is clicked more than once.)
    '''
    global running, current_time
    if not running:
        running = True
        counting(duration * 60)
        title.config(text=label_text, fg=label_color)

def starter():
    '''
    Function for start button: starts pomodoro timer
    '''
    global repeats, work, shortBreak, longBreak
    repeats += 1
    work = 25
    shortBreak = 5
    longBreak = 15

    if repeats % 8 == 0:
        start_timer(longBreak, "Long Break", red)
    elif repeats % 2 == 0:
        start_timer(shortBreak, "Short Break", red)
    else:
        start_timer(work, "Work", green)

# ----------------- button styles ------------------------------------ #

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
