"""
This File is for the designing of the game
"""
import tkinter as tk

from PIL import Image, ImageTk
import logic


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



def key_board(word, root):
    keyboard_frame = tk.Frame(root)
    keyboard_frame.grid(row=2, column=0, pady=(20, 90), padx=10, sticky="s")
    my_buttons = {}
    keyboard_layout = [['q', 'w', 'e', 'r', 't', 'z', 'u', 'i', 'o', 'p', 'ü'],
                       ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä'],
                       ['y', 'x', 'c', 'v', 'b', 'n', 'm']
                       ]


    def key_board_press(key):
        current_button = my_buttons[key]
        word_lowercase = word.lower()

        word_split = list(word_lowercase)
        logic.check_for_input(key, word)
        if key in logic.correct_letters:
            current_button.config(state =tk.DISABLED, bg='#3fde3a', fg='white', disabledforeground="white")
        else:
            current_button.config(state=tk.DISABLED, bg='#f51616', fg='white', disabledforeground="white")


    for row_index, row in enumerate(keyboard_layout):
        row_frame = tk.Frame(keyboard_frame)
        row_frame.grid(row=row_index, column=0)
        for col_index, key in enumerate(row):
            button = tk.Button(row_frame, text=key, width=7, height=3, command=lambda k=key: key_board_press(k))
            root.bind("<Key>", lambda e: key_board_press(e.char.lower()))


            button.grid(row=0, column=col_index, pady=1, padx=1)
            my_buttons[key] = button


