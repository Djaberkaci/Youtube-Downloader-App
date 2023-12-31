from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import threading


root = Tk()
root.title("Youtube Downloader")
root.geometry("600x320")
root.resizable(False,False )

#functions

def browse ():
    directory = filedialog.askdirectory(title="Save video")
    folderLink.delete(0,"end")
    folderLink.insert(0,directory)

def down_yt():
    status.config(text="text= downloading...")
    link = ytLink.get()
    folder = folderLink.get()
    YouTube(link, on_complete_callback=finsh).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(folder)
def finsh(stream=None,chunk=None,file_handle=None,remaining=None):
    status.config(text="status : Complete")


#toutube logo
ytlogo = PhotoImage(file="YouTube-Logo.png").subsample(7)
ytTitle = Label(root, image=ytlogo)
ytTitle.place(relx=0.5, rely=0.25, anchor="center")


#youtube link
ytLabel = Label(root, text="Youtube link")
ytLabel.place(x=25 , y=150)

ytLink = Entry(root,width=60)
ytLink.place(x=140, y=150)

#DownloadFolder
folderLabel = Label(root, text="Download Folder")
folderLabel.place(x=25, y=183)

folderLink= Entry(root, width=50)
folderLink.place(x=140, y=183)

#Browse btn
browse = Button(root, text="Browse",command=browse)
browse.place(x=455, y=180)

#download btn
download = Button(root, text="Download", command=threading.Thread(target=down_yt).start)
download.place(x=280, y=220)

#statusBar

status = Label(root,text="status:Ready",fg="black",bg="white",anchor="w")
status.place(rely=1,anchor="sw",relwidth=1)

root.mainloop()