import pytube
from tkinter import *

root = Tk()
root.geometry('600x400')
root.resizable(0, 0)
root.title('Youtube Downloader')

Label(root, text ='Download', font = 'arial 24 bold').pack()

link = StringVar()

Label(root, text = 'Paste your youtube link here: ', font = 'arial 18 bold').place(x=160, y=80)
link_enter = Entry(root, width = 70, textvariable = link).place(x=36, y=80)

def Downloader():
	url = pytube.YouTube(str(link.get()))
	video = url.streams.get_highest_resolution()
	video.download()
	Label(root, text = 'Video Downloaded', font = 'arial, 18').place(x=170,y=200)

Button(root, text='Download Video', font = 'arial 18 bold', bg = 'blue', padx = 2, command = Downloader).place(x=190,y=160)

root.mainloop()