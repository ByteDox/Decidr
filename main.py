import tkinter as tk
from tkinter import ttk
import random

def pick_number():
    try:
        fNum = int(fNum_var.get())
        sNum = int(sNum_var.get())
        if fNum > sNum:
            result.config(text = "First Number must be less than Second Number.")
            return
        number = random.randint(fNum, sNum)
        result.config(text = f"Your pick is: {number}")
    except ValueError:
        result.config(text = "Error: Please enter a valid number!")


root = tk.Tk()
root.title("Decidr")
root.geometry("400x240")
root.configure(bg = "#f0f0f0")
root.minsize(320, 220)

style = ttk.Style()
style.configure("TLabel", font = ("Segoe UI", 10))
style.configure("TButton", font = ("Segoe UI", 10, "bold"))
style.configure("TEntry", padding = 5)

fNum_var = tk.StringVar()
sNum_var = tk.StringVar()

main_frame = ttk.Frame(root, padding = 20)
main_frame.pack(expand = True, fill = "both")

content_frame = ttk.Frame(main_frame)
content_frame.pack(expand = True)

ttk.Label(content_frame, text = "Pick a Number Between: ").pack(pady = (0, 10))

entry_frame = ttk.Frame(content_frame)
entry_frame.pack()

ttk.Label(entry_frame, text="First Number:").grid(row = 0, column = 0, padx = 5, sticky = "e")
ttk.Entry(entry_frame, textvariable = fNum_var, width = 10).grid(row = 0, column = 1)

ttk.Label(entry_frame, text="Second Number:").grid(row = 1, column = 0, padx = 5, sticky = "e")
ttk.Entry(entry_frame, textvariable = sNum_var, width = 10).grid(row = 1, column = 1)

ttk.Button(content_frame, text = "Generate", command = pick_number).pack(pady = 15)

result = ttk.Label(content_frame, text = "", foreground = "#333", font = ("Segoe UI", 11, "bold"))
result.pack()

root.mainloop()