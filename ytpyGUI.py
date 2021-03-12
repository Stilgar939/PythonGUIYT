from pytube import Playlist
from pytube import YouTube
import tkinter as tk

def downloadYT():
    try:
        playlist = Playlist('https://www.youtube.com/playlist?list=PL2Szhg9E4zGKv96T9wuIUl6uj9ozte9Yc')

        for i in playlist:
            yt = YouTube(i)
            yt.streams.get_audio_only().download(output_path=path, filename=yt.title)    
            print('YouTube video audio downloaded successfully')

    except Exception as e:
        print(e)

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

