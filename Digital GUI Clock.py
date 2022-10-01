from tkinter import *
import time

def times():
    currentTime=time.strftime("%H: %M: %S %p")
    label.config(text=currentTime)
    label.after(200, times)

root=Tk()

root.title("Python GUI Digital Clock")
root.geometry("700x200")
root.minsize(700, 200)
root.maxsize(700, 200)

label=Label(root, font="ds-digital 100 bold", bg="black", foreground="red")
label.pack(pady=40)

times()
root.mainloop()
