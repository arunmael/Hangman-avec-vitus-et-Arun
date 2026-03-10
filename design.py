"""
This File is for the designing of the game
"""
import tkinter as tk
import logic
from PIL import Image, ImageTk


# ========== LOAD PICTURES ==========

def draw_hangman(root):
    canvas = tk.Canvas(root, width=300, height=300, bg="black")
    canvas.grid(row=0, column=0)
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


def key_board(root, random_word, random_celebritie):
    keyboard_frame = tk.Frame(root)
    keyboard_frame.grid(row=2, column=0, pady=(20, 90), padx=10, sticky="s")
    my_buttons = {}
    keyboard_layout = [['q', 'w', 'e', 'r', 't', 'z', 'u', 'i', 'o', 'p', 'ü'],
                       ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä'],
                       ['y', 'x', 'c', 'v', 'b', 'n', 'm']
                       ]

    def key_board_press(key):
        current_button = my_buttons[key]
        word_lowercase = random_word.lower()
        if logic.mode == 'classic':
            word_lowercase = random_word.lower()
        if logic.mode == 'celb':
            word_lowercase = random_celebritie.lower()
        word_split = list(word_lowercase)
        if key in word_split:
            current_button.config(highlightbackground='green', bg='green')
        else:
            current_button.config(highlightbackground='red', bg='red')
        logic.check_for_input(key, word_split)
        lines(word_split, key)

    for row_index, row in enumerate(keyboard_layout):
        row_frame = tk.Frame(keyboard_frame)
        row_frame.grid(row=row_index, column=0)
        for col_index, key in enumerate(row):
            button = tk.Button(row_frame, text=key, width=7, height=3, command=lambda k=key: key_board_press(k))
            button.grid(row=0, column=col_index, pady=1, padx=1)
            my_buttons[key] = button

    root.bind("<Key>", lambda e: key_board_press(e.char.lower()))

    line = ["_"]
    word_length = len(random_word)
    line_amount = line * word_length
    word_var = tk.StringVar(value=" ".join(line_amount))

    def lines(correct_word, key_pressed):
        line_frame = tk.Frame(root)
        line_frame.grid(row=1, column=0)

        label = tk.Label(line_frame, textvariable=word_var, font=("Arial", 40))
        label.grid(row=2, column=0)

        def refresh():
            word_var.set(" ".join(line_amount))

        for i, char in enumerate(correct_word):
            if key_pressed == char:
                line_amount[i] = char
            refresh()

            print(correct_word)

