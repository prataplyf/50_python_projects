import tkinter as tk
import random

root = tk.Tk()
root.geometry("200x200")
root.title("DiceRoll")


label = tk.Label(root, text="", font=('green', 60))

def rollDice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text='')
    label.configure(text=f'{random.choice(dice)}')
    label.pack()

button = tk.Button(root, text="Roll Dice", command=rollDice)
button.pack()

root.mainloop()

