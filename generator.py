import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("QR Code Generator")

def generate():
    bits = []
    text = entry.get()
    for j, i in enumerate(text):
        sideDict = dict(index = text[j], value = ord(i))
        mainDict = dict(sideDict)
        bits.append(mainDict)
    print(bits)





frame = tk.Frame(root)
frame.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=0)

entry_btn = tk.Button(frame, text="Generate!", command=generate)
entry_btn.grid(row=0, column=1)

root.mainloop()