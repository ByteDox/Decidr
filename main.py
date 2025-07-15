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
        result.config(text = "Error: Invalid number!")

# Clear the input and output
def clear_fields():
    fNum_var.set("")
    sNum_var.set("")
    result.config(text = "")

# Gui
root = tk.Tk()
root.title("Decidr")
root.geometry("400x240")
root.configure(bg = "#0e0e0e")
root.minsize(320, 220)

# Colors
bg_color = "#121212"
fg_color = "#e0e0e0"
accent_color = "#1f1f1f"
button_color = "#2e2e2e"
hover_color = "#3a3a3a"


# Styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background = bg_color)
style.configure("Header.TLabel", font = ("Times New Roman", 16, "bold"), foreground = "#ffffff", background = "#0e0e0e")
style.configure("SubHeader.TLabel", font = ("Times New Roman", 11), foreground = "#ffffff", background = "#0e0e0e")
style.configure("TLabel", background = bg_color, foreground = fg_color, font = ("Times New Roman", 10))
style.configure("TButton", font = ("Times New Roman", 10), background = button_color, foreground = fg_color)
style.map("TButton", background = [("active", hover_color)])
style.configure("TEntry", padding = 5, fieldbackground = accent_color, foreground = fg_color, insertcolor = fg_color)


# Variables
fNum_var = tk.StringVar()
sNum_var = tk.StringVar()


# Layout
hover_frame = tk.Frame(root, bg = "#0e0e0e")
hover_frame.place(relx = 0.5, rely = 0.5, anchor = "center")

ttk.Label(hover_frame, text = "Decidr", style = "Header.TLabel").pack(anchor = "center", pady = (0, 2))
ttk.Label(hover_frame, text = "Decisions made easy!", style = "SubHeader.TLabel").pack(anchor = "center", pady = (0, 12))

main_frame = ttk.Frame(hover_frame, padding = 16, style = "TFrame")
main_frame.pack(expand = True, fill = "both")

content_frame = ttk.Frame(main_frame)
content_frame.pack(expand = True)

ttk.Label(content_frame, text = "Pick a Number Between: ").pack(pady = (0, 10))

entry_frame = ttk.Frame(content_frame)
entry_frame.pack()

ttk.Label(entry_frame, text = "First Number:").grid(row = 0, column = 0, padx = 5, pady = 2, sticky = "e")
ttk.Entry(entry_frame, textvariable = fNum_var, width = 10).grid(row = 0, column = 1, pady = 2)

ttk.Label(entry_frame, text = "Second Number:").grid(row = 1, column = 0, padx = 5, pady = 2, sticky = "e")
ttk.Entry(entry_frame, textvariable = sNum_var, width = 10).grid(row = 1, column = 1, pady = 2)

button_frame = ttk.Frame(content_frame, style = "TFrame")
button_frame.pack(pady = (12, 5))

ttk.Button(button_frame, text = "Generate", command = pick_number).grid(row = 0, column = 0, padx = 6)
ttk.Button(button_frame, text = "Clear", command = clear_fields).grid(row = 0, column = 1, padx = 6)

result = ttk.Label(content_frame, text = "", font = ("Times New Roman", 11), foreground = "#ffffff")
result.pack()

root.mainloop()