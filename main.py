import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from tkinter import *
import pyscreenrec


root=Tk()
root.geometry("400x540")
root.title("Enregistreur d'ecran")
root.config(bg="cyan")
root.resizable(0,0)
