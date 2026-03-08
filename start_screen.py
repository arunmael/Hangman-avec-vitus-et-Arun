"""
This File is for the Start Screen
"""
import design


import tkinter as tk
import logic


def start_screen(root):
    welcome_label = tk.Label(root, text='Welcome to Hangman\n Made by Vitus and Arun', font=('Arial', 30))
    word = logic.random_word()

    def classic_button_action(event=None):
        welcome_label.place_forget()
        classic_button.place_forget()
        design.draw_hangman(root)
        design.key_board(root, word)

    classic_button = tk.Button(root, text='Classic', command=classic_button_action, font=('Arial', 30))

    classic_button.place(relx=0.5, rely=0.40, anchor='center')
    welcome_label.place(relx=0.5, rely=0.25, anchor='center')