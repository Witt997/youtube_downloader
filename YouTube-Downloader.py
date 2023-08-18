# import libraries
from tkinter import *
from pytube import YouTube, Playlist

# create the API window
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('YouTube Downloader')

# create labels
Label(root, text='Download Youtube videos for free', font=' sans-serif 15 bold').pack()
Label(root, text="Paste your link here", font="sans-serif 15 bold").place(x=150, y=55)
download_label = Label(root, text="", font="arial 15")
download_label.place(x=50, y=200)
error_label = Label(root, text="", font="arial 15")
error_label.place(x=50, y=200)

# create link cell
link_enter = Entry(root, width=70)
link_enter.place(x=30, y=85)

# functionality

# download single videos
def download_single_video(video_url):
        # captures the link and locates in YT
        url = YouTube(video_url)
        # captures the different video qualities available to download
        url.streams.filter(progressive=True, file_extension='mp4').first().download("D:\Xtreme Download Manager\Video")
        download_label.config(text="Downloaded")

# download playlists
def download_playlist(playlist):
     playlist = Playlist(playlist)
     for video in playlist.video_urls:
          print(f'Downloading: {playlist.title}')
          download_single_video(video)

def download():
    try:
        to_download = link_enter.get()
        # single or playlist?
        if "/watch?v=" in to_download:
            download_single_video(to_download)
        elif "/playlist?list=" in to_download:
            download_playlist(to_download)
        else:
            error_label.config(text="Invalid URL")
    except Exception as e:
        error_label.config(text="Error " + str(e))

 

# download button
Button(root, text="Download", font='arial 17 bold', fg='white', bg='blue', padx=2, command=download).place(x=175, y=150)

# call the GUI
root.mainloop()


# to correct the errors in the pytube cypher, change line 30 with: var_regex = re.compile(r"^\$*\w+\W")
