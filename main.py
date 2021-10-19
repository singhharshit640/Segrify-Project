"""This file is for test coding and checking output of different libraries"""

# from win10toast import ToastNotifier
# import os
# toaster = ToastNotifier()
# toaster.show_toast("Sample Notification","Python is awesome!!!")
# print(os.getcwd())
import tkinter as tk
from tkinter import filedialog
import time
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print(file_path)
__file__ = file_path


print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))

