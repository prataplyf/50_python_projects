import tkinter as tk
import random
root = tk.Tk()

count = 0
predicted_number = random.randint(0,10)
print('predicted_number: ',predicted_number)
    

def check_imagination():
    global count
    if predicted_number == int(e1.get()):
        count += 1
        res = f'{"Correct Guess, your attempt {}".format(count)}'
        myText.set(res)
    else :
        count += 1
        res = f'{"Wrong Guess in your attempt {}".format(count)}'
        myText.set(res)

myText=StringVar();
Label(root, text="Guess a number between 1 - 10").grid(row=0, columnspan=2, sticky=W)
Label(root, text="Guess The Number: ").grid(row=1, sticky=W)
Label(root, text="Result:").grid(row=3, sticky=W)
result=Label(root, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
 
e1 = Entry(root)

e1.grid(row=1, column=1)
 
b = Button(root, text="Check your Imagination", command=check_imagination)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

b = Button(root, text="Generate number", command=generate_number)
b.grid(row=2, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5) 
root.mainloop()