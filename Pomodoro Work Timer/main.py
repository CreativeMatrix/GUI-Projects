from tkinter import *
import math
from playsound import playsound
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
REPS = 0
COUNT_DOWN_TIMER = None
MARKS = ""
WORK_MIN = 0
SHORT_BREAK_MIN = 0
LONG_BREAK_MIN = 0 
   
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global MARKS, REPS, work_input, break_input, long_break_input
    window.after_cancel(COUNT_DOWN_TIMER)
    canvas.itemconfig(time_watch, text="00:00")
    timer.config(text="Timer")
    MARKS = ""
    checkmark.config(text=MARKS)
    REPS = 0

    work_input.grid(column=1, row=7)
    work_input.delete(0, last=50)
    work_input.insert(0, "Work Time")
    work_input.bind("<FocusIn>", work_text)

    break_input.grid(column=1, row=8)
    break_input.delete(0, last=50)
    break_input.insert(0, "Short Break")
    break_input.bind("<FocusIn>", break_text)

    long_break_input.grid(column=1, row=9)
    long_break_input.delete(0, last=50)
    long_break_input.insert(0, "Long Break")
    long_break_input.bind("<FocusIn>", long_break_text)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
    WORK_MIN = int(work_input.get())
    SHORT_BREAK_MIN = int(break_input.get())
    LONG_BREAK_MIN = int(long_break_input.get())
    REPS += 1
    work_input.grid_forget()
    break_input.grid_forget()
    long_break_input.grid_forget()

    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
            count_down(WORK_MIN * 60)
            timer.config(text="Work", foreground=GREEN)
            playsound("./sounds/work.mp3", block=False)
    elif REPS == 2 or REPS == 4 or REPS == 6:
            count_down(SHORT_BREAK_MIN * 60)
            timer.config(text="Break", foreground=PINK)
            playsound("./sounds/break.mp3", block=False)
    elif REPS == 8:
            count_down(LONG_BREAK_MIN * 60)
            timer.config(text="Break", foreground=RED)
            playsound("./sounds/long_break.mp3", block=False)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global COUNT_DOWN_TIMER, MARKS
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(time_watch, text=f"{count_min}:{count_sec}")
    if count > 0:
        COUNT_DOWN_TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        MARKS = ""
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            MARKS += "✔"
        checkmark.config(text=MARKS, font=(FONT_NAME, 15, "bold")) 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Work Timer".center(50))
window.config(padx=100, pady=50, background=YELLOW)

timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), background=YELLOW, foreground=GREEN)
timer.grid(column=1, row=0)

canvas = Canvas(window, width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_watch = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=5)
reset = Button(text="Reset", command=timer_reset)
reset.grid(column=2, row=5)

checkmark = Label(background=YELLOW, foreground=GREEN)
checkmark.grid(column=1, row=6)

# ---------------------------- INPUT FIELDS ------------------------------- #

def work_text(event):
   work_input.delete(0,END)

work_input = Entry(window, width=13, validate="key")
work_input.insert(0, "Work Time")
work_input.bind("<FocusIn>", work_text)
work_input.grid(column=1, row=7)

def break_text(event):
   break_input.delete(0, END)

break_input = Entry(width=13)
break_input.insert(0, "Short Break")
break_input.bind("<FocusIn>", break_text)
break_input.grid(column=1, row=8)

def long_break_text(event):
   long_break_input.delete(0, END)

long_break_input = Entry(width=13)
long_break_input.insert(0, "Long Break")
long_break_input.bind("<FocusIn>", long_break_text)
long_break_input.grid(column=1, row=9)


window.mainloop()
