import tkinter as tk
from tkinter import ttk, messagebox

def jub():
    l2.configure(text="คุณโดนตอกดาก!")
def clear():
    l2.configure(text="")


root = tk.Tk()
root.minsize(500, 500)
root.title("")
FONT = ("Times", 24)

l1 = ttk.Label(root, text="กดปุ่มเพื่อจุ้บมั้ว", font=FONT)
l1.pack(pady= 50)

b1 = ttk.Button(root, text='จุ้บมั้ว', command=jub)
b1.pack()

b2 = ttk.Button(root, text='clear', command=clear)
b2.pack(pady=20)

l2 = ttk.Label(root, font=FONT)
l2.pack(pady = 50)

root.mainloop()
