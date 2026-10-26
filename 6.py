import tkinter as tk
import random

root = tk.Tk()
root.geometry('400x400')
message = tk.StringVar()
key = tk.StringVar()
mode = tk.StringVar(value="encode")

label1 = tk.Label(root, text="Message").place(x=60, y=60)
entry_message = tk.Entry(root, textvariable=message).place(x=240, y=60)
label2 = tk.Label(root, text='Key').place(x=60, y=120)
key = tk.Entry(root, textvariable=key).place(x=240, y=120)
label3 = tk.Label(root, text="Mode").place(x=60, y=180)
radio1 = tk.Radiobutton(root, text="Encode", variable=mode, value="encode").place(x=200, y=180)
radio2 = tk.Radiobutton(root, text="Decode", variable=mode, value="decode").place(x=280, y=180)
label4 = tk.Label(root, text="Result").place(x=60, y=220)

root.mainloop()