import os
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer

c1 = '#ffffff' #white
c2 = '#6b0373' #dark
c3 = '#eb8df2' #light
c4 = '#333133' #grey

window = Tk()
window.title("")
window.geometry('455x355')
window.configure(background=c1)
window.resizable(width=FALSE, height=FALSE)

#events
def play_music():
    running = listbox.get(ACTIVE)
    print("running : ", running)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def next_music():
    playing = running_song['text']
    index = songs.index(playing)
    size = len(songs)
    new_index = (index % (size-1)) + 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

def prev_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index - 1;
    if new_index == 0 :
        new_index = len(songs) -1;

    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

#frames
left_frame = Frame(window, width=225, height=225, bg=c1)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(window, width=225, height=250, bg=c4)
right_frame.grid(row=0, column=1, padx=0)

down_frame = Frame(window, width=500, height=200, bg=c3)
down_frame.grid(row=1, column=0, columnspan=3, padx=0, pady=1)

#right frame
listbox = Listbox(right_frame, selectmode=SINGLE, font=("Arial 15 bold"), width=30, bg=c4, fg=c1)
listbox.grid(row=0, column=0)

w = Scrollbar(right_frame)
w.grid(row=0, column=1)

listbox.config(yscrollcommand=w.set)
w.config(command= listbox.yview)

#images
img_1 = Image.open('/Users/janhavidalal/Downloads/icons/music.png')
img_1 = img_1.resize((200,200))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, height=210, image= img_1, padx=10, bg=c1)
app_image.place(x=10, y=15)

img_2 = Image.open('/Users/janhavidalal/Downloads/icons/previous.png')
img_2 = img_2.resize((90,90))
img_2 = ImageTk.PhotoImage(img_2)
prev_button = Button(down_frame, width=80,height=80, image= img_2, padx=10, bg=c3, font=("Ivy 10"),command=prev_music)
prev_button.place(x=45, y=30)

img_3 = Image.open('/Users/janhavidalal/Downloads/icons/play.png')
img_3 = img_3.resize((70,70))
img_3 = ImageTk.PhotoImage(img_3)
play_button = Button(down_frame, width=80,height=80, image= img_3, padx=10, bg=c3, font=("Ivy 10"), command=play_music)
play_button.place(x=90+45, y=30)

img_4 = Image.open('/Users/janhavidalal/Downloads/icons/next.png')
img_4 = img_4.resize((90,90))
img_4 = ImageTk.PhotoImage(img_4)
next_button = Button(down_frame, width=80,height=80, image= img_4, padx=10, bg=c3, font=("Ivy 10"), command=next_music)
next_button.place(x=180+45, y=30)

img_5 = Image.open('/Users/janhavidalal/Downloads/icons/pause.png')
img_5 = img_5.resize((90,90))
img_5 = ImageTk.PhotoImage(img_5)
pause_button = Button(down_frame, width=80,height=80, image= img_5, padx=10, bg=c3, font=("Ivy 10"), command=pause_music)
pause_button.place(x=270+45, y=30)

running_song = Label(down_frame, text="Choose a Song", font=("Ivy 15"), width=70, height=1, padx=10, bg=c1, fg=c4, anchor=NW)
running_song.place(x=0, y=1)

os.chdir(r'/Users/janhavidalal/Downloads/SongsPython')
songs = os.listdir()

def show():
    for i in songs:
        if(".mp3" in i) :
            listbox.insert(END, i)

show()

mixer.init()
music_state = StringVar()
music_state.set("Choose one!")

window.mainloop()