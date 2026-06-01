import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("QR Code Generator")



def convert_to_binary(number):
    res = ""
    while number > 0:
        res += str(number%2)
        number //= 2
    return(res[::-1]).zfill(8)

def generate():
    bits = "0100"
    text = entry.get()
    bits += convert_to_binary(len(text)).zfill(8)
    for i in text:
        bits +=  convert_to_binary(ord(i))
    bits += "0000"
    print(bits)


frame = tk.Frame(root)
frame.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=0)

entry_btn = tk.Button(frame, text="Generate!", command=generate)
entry_btn.grid(row=0, column=1)

root.mainloop()