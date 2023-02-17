import tkinter as tk
import pytube
import tkinter.filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from art import *
from pytube import YouTube
from pytube import Playlist 

from tkinter import messagebox

def browse_folder():
    folder = tk.filedialog.askdirectory()
    entry_folder.insert(0, folder)

root = tk.Tk()
root.title("YouTube Music Downloader")
root.geometry("400x400")


download_var =  tk.IntVar()

rb1 = ttk.Radiobutton(root, text='jednotlivá píseň', variable=download_var, value=1, bootstyle="secondary")
rb2 = ttk.Radiobutton(root, text='playlist', variable=download_var, value=2, bootstyle="secondary")
rb3 = ttk.Radiobutton(root, text='video', variable=download_var, value=3, bootstyle="secondary")
rb4 = ttk.Radiobutton(root, text='video playlist', variable=download_var, value=4, bootstyle="secondary")

frame_link = tk.Frame(root)
frame_link.grid(padx=10, pady=10)
frame_link.pack()
""" Definuju základní prvky a rozložení. Naskládají se dle pořadí zavolání metody pack."""

vyber_typ = tk.Frame(root)
vyber_typ.pack()
rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()



label = tk.Label(root)
label.pack()

def download():
    if download_var.get()==1:
        link = entry_link.get()
        folder = entry_folder.get()
        yt = pytube.YouTube(link)
        stream = yt.streams.filter(only_audio=True).first()
        out_file= stream.download(folder)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        files_downloaded.set(files_downloaded.get() + 1)

    elif download_var.get()==2:
        link = entry_link.get() 	
        folder = entry_folder.get()
        url = Playlist(link)
        videos = url.video_urls
        for video in url.videos:
            music = video.streams.filter(only_audio=True).first()
            out_file= music.download(folder)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            files_downloaded.set(files_downloaded.get() + 1)

       










    elif download_var.get()==3:
        link = entry_link.get()
        folder = entry_folder.get()
        yt = pytube.YouTube(link)
        youtubeObject = yt.streams.get_highest_resolution()
        youtubeObject.download(folder)
        files_downloaded.set(files_downloaded.get() + 1)

    elif download_var.get()==4:
        link = entry_link.get() 	
        folder = entry_folder.get()
        url = Playlist(link)
       
        for video in url.videos:
            music = video.streams.get_highest_resolution()
            out_file= music.download(folder)
            files_downloaded.set(files_downloaded.get() + 1)
            









label_link = tk.Label(frame_link, text="Vlož youtube odkaz:")
label_link.pack(pady= 10)
label_link.pack(side="left")

vyber_typ = tk.Label(vyber_typ, text="Vyber typ, který chceš stáhnout")
vyber_typ.pack(pady= 10)
vyber_typ.pack(side="left")


entry_link = tk.Entry(frame_link)
entry_link.pack(side="right")

frame_folder = tk.Frame(root)
frame_folder.pack()

label_folder = tk.Label(frame_folder, text="Vyber složku")
label_folder.pack(side="left")

entry_folder = tk.Entry(frame_folder)
entry_folder.pack(side="left")

button_folder = ttk.Button(frame_folder, text="procházet", command=browse_folder)
button_folder.pack(side="right")

button_download = ttk.Button(root, text="stáhnout", command=download, bootstyle=SUCCESS)
button_download.pack()


pocet = tk.Frame(root)
pocet.pack()
pocet = tk.Label(pocet, text="Počet stažených souborů")
pocet.pack(pady= 10)
pocet.pack(side="left")

files_downloaded = ttk.IntVar(value=0)
files_downloaded_label = ttk.Label(root, textvariable=files_downloaded)
files_downloaded_label.pack()

root.mainloop()