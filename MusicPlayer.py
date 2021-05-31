from tkinter.constants import BOTH, BOTTOM, CENTER, LEFT, RIGHT, TOP, X, Y, YES
import pygame
import os 
import tkinter as tk 
from tkinter.filedialog import askdirectory
from PIL import Image , ImageTk
#Function 
def play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()
def ExitMusicPlayer():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def resume():
    pygame.mixer.music.unpause()

#Wedget Managing
window = tk.Tk()
window.geometry('1280x1280')
window.title('MusicPlayer')
#-----Frames------------------------
Top_frame=tk.Frame(window,width=1080,height=500,bg='#3A3A3A')
Bottom_frame=tk.Frame(window,width=1080,height=580,bg='#474545')

#prompt the user to choose a directory
directory = askdirectory()

#used to change the current working directory to specified path #GeeksforGeeks
os.chdir(directory)

#os.listdir() returns a list conatining the names of the entries in the directory given by path.
songlist = os.listdir()
#the scrollbar
scrollbar = tk.Scrollbar(Bottom_frame)
scrollbar.pack( side = RIGHT, fill = Y )
#The playlist
playlist = tk.Listbox(Bottom_frame,width=1080,font='Gotham',bg='#3A3A3A' ,fg='#DCDBDB',selectmode=tk.SINGLE,yscrollcommand=scrollbar.set)
#creating Images 
load=Image.open('/Musik.png')
height=300
width=300
photo=ImageTk.PhotoImage(load)
canvas=tk.Canvas(Top_frame,bg='Black',bd='0',width=width,height=height)
canvas.create_image(height/2,width/2,image=photo)
canvas.place(x=513,y=10)

#Adding songs from songlist to play list
for item in songlist:
    pos =0 
    playlist.insert(pos,item)
    pos += 1

#Initialaising module
pygame.init()
pygame.mixer.init()


var = tk.StringVar()

#Creating buttons
Btn1 = tk.Button(Top_frame, width=15, height=2, font="Cambria 20 bold", text="Play Music", command=play,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0') 
Btn2 = tk.Button(Top_frame, width=15, height=2, font="Cambria 20 bold", text="Stop Music", command=ExitMusicPlayer,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0') 
Btn3 = tk.Button(Top_frame, width=15, height=2, font="Cambria 20 bold", text="Pause Music", command=pause,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0') 
Btn4 = tk.Button(Top_frame, width=15, height=2, font="Cambria 20 bold", text="Resume Music", command=resume,bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0')

#creating Label 
song_title =tk.Label(Top_frame,height=3,width=150,textvariable=var,bd='0',bg='#343434',fg='#DCDBDB',font='Gotham',justify=CENTER)

#adding the buttons to the frame 
Top_frame.pack(side=TOP,fill=BOTH ,expand=YES)
Bottom_frame.pack(side=BOTTOM,fill=BOTH ,expand=YES)
song_title.place(x=10,y=320)
Btn1.place(x=110,y=400)
Btn2.place(x=379,y=400)
Btn3.place(x=648,y=400)
Btn4.place(x=917,y=400)
canvas.place(x=490,y=10)
playlist.pack(fill=BOTH ,expand=YES)
window.mainloop()