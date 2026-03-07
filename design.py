"""
This File is for the desing of the game
"""
import tkinter as tk

root = tk.Tk()
root.title("Hangman")
root.geometry("1200x700")


def key_board():
    keyboard_frame = tk.Frame(root)
    keyboard_frame.pack(pady=(20, 90), padx=10, side='bottom')
    my_buttons = {}
    keyboard_layout = [['q', 'w', 'e', 'r', 't', 'z', 'u', 'i', 'o', 'p', 'ü'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä'],
        ['y', 'x', 'c', 'v', 'b', 'n', 'm']
    ]

    word = 'Hello' #bis es eine word Variable gibt!!!!! Dann löschen
    
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


key_board()
root.mainloop()