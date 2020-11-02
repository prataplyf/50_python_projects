from tkinter import *
from tkinter import messagebox
import time


# creating Tk window
root = Tk()

# setting geometry of tk window
root.geometry("200x150")

# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Time Counter")

# Variables Declaration
hour=StringVar()
minute=StringVar()
second=StringVar()

# setting the default value as 0 of Hour, Minutes, Seconds
hour.set("00")
minute.set("00")
second.set("00")

# Use of Entry class to take input from the user
hourEntry= Entry(root, width=3, font=("Arial",20,""),
				textvariable=hour)
hourEntry.place(x=30,y=20)

minuteEntry= Entry(root, width=3, font=("Arial",20,""),
				textvariable=minute)
minuteEntry.place(x=80,y=20)

secondEntry= Entry(root, width=3, font=("Arial",20,""),
				textvariable=second)
secondEntry.place(x=130,y=20)


def submit():
	try:
		# the input provided by the user is
		# stored in here :temp
		temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except:
		print("Please input the right value")
	while temp >-1:
		
		# divmod(firstvalue = temp//60, secondvalue = temp%60)
		mins,secs = divmod(temp,60) 

		# Converting the input entered in mins or secs to hours,
		# mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
		# 50min: 0sec)
		hours=0
		if mins >60:
			
			# divmod(firstvalue = temp//60, secondvalue 
			# = temp%60)
			hours, mins = divmod(mins, 60)
		
		# using format () method to store the value up to 
		# two decimal places
		hour.set("{00:2d}".format(hours))
		minute.set("{00:2d}".format(mins))
		second.set("{00:2d}".format(secs))

		# updating the GUI window after decrementing the
		# temp value every time
		root.update()
		time.sleep(1)

		# when temp value = 0; then a messagebox pop's up
		# with a message:"Time's up"
		if (temp == 0):
			messagebox.showinfo("Time Counter", "Time's up")
		
		# after every one sec the value of temp will be decremented
		# by one
		temp -= 1

# button widget
btn = Button(root, text='Start Countdown', bd='5', bg="#abc123",
			command= submit)
btn.place(x = 30,y = 80)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()
