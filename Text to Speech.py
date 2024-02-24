import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from tkinter import Tk, Frame, Label, PhotoImage, Button
import googletrans
from googletrans import Translator

root = Tk()
root.title("KD Translator 3.0")
root.geometry("900x700+200+200")
root.resizable(False,False)
root.configure(bg="#305065")


#operation
def label_change():
    c=language_combo.get()
    c1=language_combo2.get()
    language1.configure(text=c)
    language2.configure(text=c1)
    root.after(1000,label_change)

def translate_now():
    text_=text_area.get(1.0,END)
    t1=Translator()
    trans_text=t1.translate(text_,src=language_combo.get(),dest=language_combo2.get())
    trans_text=trans_text.text

    text_area2.delete(1.0,END)
    text_area2.insert(END,trans_text)
    
    
engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

            
def speaknow1():
    text1 = text_area2.get(1.0, END)
    gender1 = gender_combobox2.get()
    speed1 = speed_combobox2.get()
    voices1 = engine.getProperty('voices')

    def setvoice1():
        if (gender1 == 'Male'):
            engine.setProperty('voice', voices1[0].id)
            engine.say(text1)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices1[1].id)
            engine.say(text1)
            engine.runAndWait()

    if (text1):
        if (speed1 == "Fast"):
            engine.setProperty('rate', 250)
            setvoice1()
        elif (speed1 == "Normal"):
            engine.setProperty('rate', 150)
            setvoice1()
        else:
            engine.setProperty('rate', 60)
            setvoice1()

def download1():
    text1 = text_area2.get(1.0, END)
    gender1 = gender_combobox2.get()
    speed1= speed_combobox2.get()
    voices1 = engine.getProperty('voices')

    def setvoice1():
        if (gender1 == 'Male'):
            engine.setProperty('voice', voices1[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text1,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices1[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text1,'text.mp3')
            engine.runAndWait()

    if (text1):
        if (speed1 == "Fast"):
            engine.setProperty('rate', 250)
            setvoice1()
        elif (speed1 == "Normal"):
            engine.setProperty('rate', 150)
            setvoice1()
        else:
            engine.setProperty('rate', 60)
            setvoice1()
            

#icon
image_icon=PhotoImage(file="1333.png")
root.iconphoto(False,image_icon)

#Top Frame
top_frame_width = 1000
top_frame_height = 100

Top_frame = Frame(root, bg="white", width=top_frame_width, height=top_frame_height)
Top_frame.place(x=0, y=0)

logo = PhotoImage(file="1233.png")

resized_logo = logo.subsample(max(1, int(logo.width() / 80)), max(1, int(logo.height() / 80)))

label_logo = Label(Top_frame, image=resized_logo, bg="white")
label_logo.place(x=20, y=8)

Label(Top_frame,text="TRANSLATOR & TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=105,y=35)

#Language_selection
language = googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

language_combo=Combobox(root,values=languageV,font="Roboto 14",state="r")
language_combo.place(x=35,y=155)
language_combo.set("English")

language1=Label(root,text="English",font="segoe 20 bold",bg="white", width=11,bd=5,relief=GROOVE)
language1.place(x=300,y=145)


#Input Box
text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=20,y=200,width=500,height=150)

scrollbar1=Scrollbar(text_area)
scrollbar1.pack(side="right",fill='y')

scrollbar1.configure(command=text_area.yview)
text_area.configure(yscrollcommand=scrollbar1.set)


#Gender_selection
Label(root,text="Voice",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=200)
gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=230)
gender_combobox.set('Male')


#Speed_selection
Label(root,text="Speed",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=200)
speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=730,y=230)
speed_combobox.set('Normal')


#Speak
imageicon=PhotoImage(file="1444.png")
small_icon = imageicon.subsample(15)
btn=Button(root,text="Speak",compound=LEFT,image=small_icon,width=118,font="arial 14 bold",command=speaknow)
btn.pack()
btn.place(x=553,y=280)


#Save
imageicon2=PhotoImage(file="1555.png")
small_icon2 = imageicon2.subsample(15)
sav=Button(root,text="Save",compound=LEFT,image=small_icon2,width=118,font="arial 14 bold",command=download)
sav.pack()
sav.place(x=733,y=280)


#Translate Button
translate=Button(root,text="Translate",font=("Roboto",15),activebackground="white",cursor="hand2",
                 bd=1,width=10,height=2,bg="black",fg="white",command=translate_now)
translate.place(x=200,y=370)


#######################################################################################################################


#Language_selection
language_combo2=Combobox(root,values=languageV,font="Roboto 14",state="r")
language_combo2.place(x=35,y=455)
language_combo2.set("SELECT LANGUAGE")

language2=Label(root,text="English",font="segoe 17 bold",bg="white", width=14,bd=5,relief=GROOVE)
language2.place(x=300,y=450)


#Input Box
text_area2=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area2.place(x=20,y=500,width=500,height=150)

scrollbar2=Scrollbar(text_area2)
scrollbar2.pack(side="right",fill='y')

scrollbar2.configure(command=text_area2.yview)
text_area2.configure(yscrollcommand=scrollbar2.set)


#Gender_selection
Label(root,text="Voice",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=505)
gender_combobox2=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender_combobox2.place(x=550,y=535)
gender_combobox2.set('Male')


#Speed_selection
Label(root,text="Speed",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=505)
speed_combobox2=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox2.place(x=730,y=535)
speed_combobox2.set('Normal')


#Speak
imageicon3=PhotoImage(file="1444.png")
small_icon3 = imageicon3.subsample(15)
btn2=Button(root,text="Speak",compound=LEFT,image=small_icon3,width=118,font="arial 14 bold",command=speaknow1)
btn2.pack()
btn2.place(x=553,y=584)


#Save
imageicon4=PhotoImage(file="1555.png")
small_icon4 = imageicon4.subsample(15)
sav2=Button(root,text="Save",compound=LEFT,image=small_icon4,width=118,font="arial 14 bold",command=download1)
sav2.pack()
sav2.place(x=733,y=584)


label_change()

root.mainloop()

