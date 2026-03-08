"""
This File is for the Start Screen
"""
import design


import tkinter as tk
import logic


def start_screen(root):
    welcome_label = tk.Label(root, text='Welcome to Hangman\n Made by Vitus and Arun', font=('Arial', 30))
    word = logic.random_word()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    def classic_button_action(event=None):
        welcome_label.grid_forget()
        classic_button.grid_forget()

        design.draw_hangman(root)
        design.key_board(root, word)

    classic_button = tk.Button(root, text='Classic', command=classic_button_action, font=('Arial', 30))

    classic_button.grid(row=1, column=0, sticky='ns')
    welcome_label.grid(row=0, column=0, pady=10, sticky='ns')