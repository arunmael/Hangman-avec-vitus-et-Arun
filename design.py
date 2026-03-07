"""
This File is for the designing of the game
"""
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Hangman")
root.geometry("300x400")

canvas = tk.Canvas(root, width=300, height=300, bg="black")
canvas.grid(row=0, column=0)

# ========== LOAD PICTURES ==========

hangman = [] # wird gebraucht um das PNG zu
for i in range(1, 14):
    img = Image.open(f"hangman_images/stage{i}.png")
    img = img.resize((300, 300))
    photo = ImageTk.PhotoImage(img)
    hangman.append(photo)



image_ids = []
count = 0

# ========== FUNCTIONS ==========

def draw_stage():
    global count
    created_image = canvas.create_image(150, 150, image=hangman[count])
    image_ids.append(created_image)
    count += 1

def remove_stage():
    global count
    last_image = image_ids.pop()
    canvas.delete(last_image)
    count -= 1

# ========== Buttons ==========

btn_frame = tk.Frame(root)
btn_frame.grid(row=1, column=0)

backward_btn = tk.Button(btn_frame, text="Back", command=remove_stage) # removes hangman stage
forward_btn = tk.Button(btn_frame, text="Forward", command=draw_stage) # adds hangman stage
backward_btn.grid(row=1, column=0)
forward_btn.grid(row=1, column=1)



def key_board_normal():
    tastatur = tk.Frame(root, bg="#2b2b2b")
    tastatur.pack(pady=20)

    zeilen = [
        ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
        ['Y', 'X', 'C', 'V', 'B', 'N', 'M']
    ]

def wrong_letter():
    pass


def false_postionn():
    pass


def right_letter():
    pass



root.mainloop()