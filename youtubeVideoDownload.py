# Importing necessary packages 
import tkinter as tk 
from tkinter import *
from pytube import YouTube 
from tkinter import messagebox, filedialog 


# Defining CreateWidgets() function 
# to create necessary tkinter widgets 
def Widgets(): 
	link_label = Label(root, text="YouTube link", bg="#E8D579") 
	link_label.grid(row=1, column=0, pady=5, padx=5) 

	root.linkText = Entry(root, width=55, textvariable=video_Link) 
	root.linkText.grid(row=2, column=0, pady=5, padx=5, columnspan = 2) 

	browse_B = Button(root, text="Browse", command=Browse, width=10, bg="#05E8E0") 
	browse_B.grid(row=4, column=0, pady=5, padx=5) 

	root.destinationText = Entry(root, width=55, textvariable=download_Path) 
	root.destinationText.grid(row=5, column=0, pady=5, padx=5) 	

	Download_B = Button(root, text="Download", command=Download, width=20, bg="#05E8E0") 
	Download_B.grid(row=6, column=0, pady=3, padx=3) 

# Defining Browse() to select a 
# destination folder to save the video 

def Browse(): 
	# Presenting user with a pop-up for directory selection. initialdir 
	# argument is optional Retrieving the user-input destination directory and 
	# storing it in downloadDirectory 
	download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH") 

	# Displaying the directory in the directory 
	# textbox 
	download_Path.set(download_Directory) 

# Defining Download() to download the video 
def Download(): 
	
	# getting user-input Youtube Link 
	Youtube_link = video_Link.get()
	print("link: " + Youtube_link)
	# select the optimal location for 
	# saving file's 
	download_Folder = download_Path.get()

	# Creating object of YouTube() 
	getVideo = YouTube(Youtube_link) 

	# Getting all the available streams of the 
	# youtube video and selecting the first 
	# from the 
	videoStream = getVideo.streams.first() 

	# Downloading the video to destination 
	# directory 
	videoStream.download(download_Folder) 

	# Displaying the message 
	messagebox.showinfo("SUCCESSFULLY", 
						"DOWNLOADED AND SAVED IN\n"
						+ download_Folder) 

# Creating object of tk class 
root = tk.Tk() 

# Setting the title, background color 
# and size of the tkinter window and 
# disabling the resizing property 
root.geometry("470x200") 
root.resizable(False, False) 
root.title("YouTube Video Downloader") 
root.config(background="#000000") 

# Creating the tkinter Variables 
video_Link = StringVar() 
download_Path = StringVar() 

# Calling the Widgets() function 
Widgets() 

# Defining infinite loop to run 
# application 
root.mainloop() 
