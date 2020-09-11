import tkinter as tk
from tkinter import Button
from Recognizer import recognize
from PIL import Image, ImageTk
import os
import time


def say_something():
    s = recognize()
    output_text_area.delete(1.0, tk.END)
    output_text_area.insert(1.0, s)


def show_signs():
    s = output_text_area.get(1.0, tk.END)
    b = list(s)
    lst = list(s)
    for i in range(len(lst)):
        c = str(lst[i]).capitalize()
        if c == " ":
            b = "-.jpg"
        else:
            b = c+".jpg"

        if os.path.exists("signs/" + b):
            temp_sign_img = Image.open("signs/" + b)
            temp_sign_photo = ImageTk.PhotoImage(temp_sign_img)
            sign_image_lbl = tk.Label(root, bg="white", image=temp_sign_photo)
            sign_image_lbl.place(x=540, y=61, width=800, height=588)
            root.update_idletasks()
        else:
            pass

        time.sleep(1)

    reject_string()


def reject_string():
    output_text_area.delete(1.0, tk.END)


root = tk.Tk()
root.title("Deaf Communicator")
root.state('normal')

image = Image.open("images/android_mic.jpg")
photo = ImageTk.PhotoImage(image)

project_name_label = tk.Label(root, text="Deaf Communicator", fg="black", font="Times 30 bold")
project_name_label.place(x=550, y=10, width=400, height=50)

mic_button = Button(root, image=photo, bg="white", command=say_something)
mic_button.place(x=10, y=60, width=500, height=236)

say_something_button = Button(root, text='Say Something !', bg="green", fg="white", font="Times 20 bold", width=25, height=2, command=say_something)
say_something_button.place(x=10, y=310, width=500, height=50)

text_area_label = tk.Label(root, text="User Said", fg="black", font="Times 30 bold")
text_area_label.place(x=-110, y=370, width=400, height=60)

output_text_area = tk.Text(font="Times 16 bold")
output_text_area.place(x=10, y=440, width=500, height=200)

accept_button = Button(root, text='Play', bg="green", fg="white", font="Times 20 bold", width=25, height=2, command=show_signs)
accept_button.place(x=10, y=650, width=500, height=50)

sign_image_label = tk.Label(root, bg="white")
sign_image_label.place(x=540, y=61, width=800, height=637)

root.geometry("500x300+100+100")  # Width x Height
root.mainloop()
