import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from tkinter import *
import pyscreenrec


root=Tk()
root.geometry("360x540")
root.title("Enregistreur d'ecran")
root.config(bg="cyan")
root.resizable(0,0)


# creations des fx
def start_enr():
    file=Filename.get()
    enr.start_recording(str(file+".mp4"),55)
    freq=48000
    duration=55
    
    recording = sd.rec(int(duration*freq), samplerate=freq, channels=2)
    sd.wait()
    write("recording.wav", freq, recording)
    
def pause_enr():
    enr.pause_recording()

def stop_enr():
    enr.stop_recording()
    
    
# var 
enr=pyscreenrec.ScreenRecorder()   

# icode de l'app
image_icon=PhotoImage(file="img/logo.png")
root.iconphoto(False, image_icon)

# image d'arriere plan
# image_bg1=PhotoImage(file="bg.png")
# Label(root, image=image_bg1, bg="#fff").place(x=2, y=100)
# image_bg2=PhotoImage(file="bg.png")
# Label(root, image=image_bg2, bg="#fff").place(x=180, y=220)

# title
lbl=Label(root, text="Enregisteur d'ecran", bg="white", font="arial 13 bold")
lbl.pack(padx=10, pady=10)

image_bg3=PhotoImage(file="img/btn.png")
Label(root, image=image_bg3).pack(pady=50)

# les entrees
Filename=StringVar()
# entry=Entry(root, textvariable=Filename, width=18, font="arial 13")
# entry.place(x=50, y=350)
# Filename.set("Enreistrer")

img4=PhotoImage(file="img/pause.png")
pause=Button(root, image=img4, bd=0, bg="#fff", command=pause_enr)
pause.place(x=50, y=450)

img5=PhotoImage(file="img/play.png")
play=Button(root, image=img5, bd=0, bg="#fff", command=start_enr)
play.place(x=150, y=450)

img6=PhotoImage(file="img/stop.png")
stop=Button(root, image=img6, bd=0, bg="#fff", command=stop_enr)
stop.place(x=250, y=450)
  
# on demarre la frm
root.mainloop()