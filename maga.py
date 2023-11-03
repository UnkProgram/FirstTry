import tkinter as tk
from random import randint, choice
from tkinter import messagebox

window = tk.Tk()

window.resizable(width = False, height = False )

window.title("Кнопки")

window.geometry('720x360')

window["bg"] = "black"

idea = tk.Label( window, text = "Добавить кнопку", font = ("Arial Bold", 15), fg = "lime",bg = "black")
idea.place(x = 290, y = 25)
window.mainloop()