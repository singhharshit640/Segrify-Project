import eel
import mainscript as m
import tkinter as tk
from tkinter import filedialog

eel.init("templates")
eel.start("index.html", block=False, size=(600, 700))


@eel.expose
def run(path):
    r = m.segragete(path)
    eel.result(r)


@eel.expose
def selectFolder():
    root = tk.Tk()
    root.withdraw()

    directory_path = filedialog.askdirectory()
    print(directory_path)
    eel.setvalue(directory_path)


while True:
    eel.sleep(10)

    
