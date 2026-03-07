"""
This File is for the desing of the game
"""
import tkinter as tk
import logic

root = tk.Tk()
root.title("Hangman")
root.geometry("700x700")
root.configure(bg="#41423d")

canvas = tk.Canvas(root, width=300, height=300, bg="black")
canvas.grid(row=0, column=0)

# ========== LOAD PICTURES ==========

def draw_hangman():

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
        nonlocal count
        created_image = canvas.create_image(150, 150, image=hangman[count])
        image_ids.append(created_image)
        count += 1

    def remove_stage():
        nonlocal count
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


# ========== KEYBOARD FUNCTIONS ==========



def key_board(word, root):
    keyboard_frame = tk.Frame(root)
    keyboard_frame.pack(pady=(20, 90), padx=10, side='bottom')
    my_buttons = {}
    keyboard_layout = [['q', 'w', 'e', 'r', 't', 'z', 'u', 'i', 'o', 'p', 'ü'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä'],
        ['y', 'x', 'c', 'v', 'b', 'n', 'm']
    ]


    
    def key_board_press(key):
        current_button = my_buttons[key]
        word_lowercase = word.lower()

        word_split = list(word_lowercase)
        if key in word_split:
            current_button.config(highlightbackground='green')
        else:
            current_button.config(highlightbackground='red')



    for row_index, row in enumerate(keyboard_layout):
        row_frame = tk.Frame(keyboard_frame)
        row_frame.pack()
        for col_index, key in enumerate(row):
            button = tk.Button(row_frame, text=key, width=7, height=3, command=lambda k=key: key_board_press(k))
            root.bind("<Key>", lambda e: key_board_press(e.char.lower()))
            button.pack(side='left', pady=1, padx=1)
            my_buttons[key] = button

