from gtts import gTTS
import os
from tkinter import *
def savee():
    
    playtext=text_entrytext.get()+"\n"
    f = open("google_text_to_speech.txt",'a')
    f.write(playtext)
    f.close()
def play():

    fh=open("google_text_to_speech.txt","r" )
    mytext=fh.read().replace("\n","")
    language ="en"
    output=gTTS(text=mytext,lang=language,slow=False)
    output.save("output.mp3")
    fh.close()
    os.system("output.mp3")

teext=Tk()
teext.title(" txt to speech converter")
teext.geometry("1000x1000")
teext["bg"] = "#118800"
title_label = Label(teext, text="Text to speech converter", font = ("Calibri", 40, "bold"),bg="#118800",fg="#000000")
title_label.grid(row = 0, column = 0,padx=20,pady=20)
frame1= Frame(teext,bg="#065535")
frame1.grid(pady=21)

text_label = Label(frame1, text="enter your text", font = ("Calibri", 35),bg="#065535",fg="#ff0000")
text_label.grid(row = 3, column = 0,padx=20,pady=20)

#textbox - Entry text
text_entrytext = Entry(frame1, font=("Aerial", 25))
text_entrytext.grid(row = 3, column = 1,padx=20,pady=20)
button_submit = Button(frame1, text="save to text file",command=savee, width=25, font="Calibri 20")
button_submit.grid(row=4,column=0,padx=20,pady=20)

button_submit1 = Button(frame1, text="play/convert to speech",command=play, width=25, font="Calibri 20")
button_submit1.grid(row=4,column=1,padx=20,pady=20)

#Dictionary method for changing attributes of button
button_submit["fg"] = "white"
#windows users
button_submit["bg"] = "#f88104"
teext.mainloop()