import tkinter as tk
import math


# ======= CONSTANTS =======
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SEC = 60
WIDTH = 300
HEIGHT = 300
reps = 0
checkmarks = 0
timer = None


# ======= TIMER RESET =======
def reset_timer():

    global reps, timer

    window.after_cancel(timer)
    reps = 0
    timer_lbl.config(text="Timer", foreground=GREEN)
    checkmark_lbl.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ======= TIMER MECHANISM =======
def start_timer():

    global reps
    reps += 1

    work_sec = WORK_MIN*SEC
    short_break_sec = SHORT_BREAK_MIN*SEC
    long_break_sec = LONG_BREAK_MIN*SEC

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_lbl["text"] = "Break"
        timer_lbl.config(foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_lbl["text"] = "Break"
        timer_lbl.config(foreground=PINK)
    else:
        count_down(work_sec)
        timer_lbl["text"] = "Work"
        timer_lbl.config(foreground=GREEN)


# ======= COUNTDOWN MECHANISM =======
def count_down(count):
    global reps, checkmarks, timer

    count_min = math.floor(count/SEC)
    count_sec = count % SEC
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    elif count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks = "✓"*int(reps/2)
            checkmark_lbl.config(text=f"{checkmarks}")


# ======= UI SETUP =======

# Window
window = tk.Tk()
window.title("Pomodoro App")
window.minsize(WIDTH, HEIGHT)
window.config(padx=WIDTH/10, pady=HEIGHT/10, background=YELLOW)
window.iconbitmap("pomodoro.ico")

# Tomato image
canvas = tk.Canvas(width=WIDTH, height=HEIGHT, background=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image((WIDTH/2), (HEIGHT/2), image=tomato_img)
timer_text = canvas.create_text((WIDTH/2), (HEIGHT/2+HEIGHT/20), text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_btn = tk.Button(text="Start", highlightthickness=0, command=start_timer)
reset_btn = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
start_btn.grid(column=0, row=2, sticky="e")
reset_btn.grid(column=2, row=2, sticky="w")

# Labels
timer_lbl = tk.Label(text="Timer", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 28, "bold"))
timer_lbl.grid(column=1, row=0, sticky="s")

# Checkmark
checkmark_lbl = tk.Label(background=YELLOW, foreground=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark_lbl.grid(column=1, row=3, sticky="n")


window.mainloop()
