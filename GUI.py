from pytube import Playlist
from pytube import YouTube
import tkinter as tk

def downloadYT():
    print("download")

path = '/home/stilgar/Escritorio/Clot/Free/YotubePy/musica'

window = tk.Tk()
window.title("Youtube downloader")
#label = tk.Label(text="Python rocks!")
#label.pack()

btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=downloadYT  # <--- Add this line
)

window.mainloop()

