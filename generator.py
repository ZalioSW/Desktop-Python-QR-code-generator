import tkinter as tk
from tkinter import messagebox, PhotoImage
import qrcode
from PIL import Image, ImageTk

root = tk.Tk()
root.title("QR Code Generator")


counter = 1

frame = tk.Frame(root)
frame.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=0)

image_label = tk.Label(frame)
image_label.grid(row=1, column=0)

def generate():
    global counter
    qr = qrcode.QRCode()
    text = entry.get()
    qr.add_data(text)
    img = qr.make_image()
    filename = f"./images/qrcode{counter}.png"
    img.save(filename)
    pil_img = Image.open(filename)
    tk_image = ImageTk.PhotoImage(pil_img)
    print("QR code generated!")
    tk_image = PhotoImage(file=f"./images/qrcode{counter}.png")
    image_label.configure(image=tk_image)
    counter += 1

entry_btn = tk.Button(frame, text="Generate!", command=generate)
entry_btn.grid(row=2, column=0)

    



root.mainloop()