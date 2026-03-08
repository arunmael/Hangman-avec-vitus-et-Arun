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
        classic_label = tk.Label(root, text='Classic', font=('Arial', 30))
        classic_label.place(x=15, y=15)

    def celebrities_button_action(event=None):
        welcome_label.place_forget()
        celebrities_button.place_forget()
        design.draw_hangman(root)
        design.key_board(root, word)
        celb_label = tk.Label(root, text='Celebrity', font=('Arial', 30))
        celb_label.place(x=15, y=15)

    classic_button = tk.Button(root, text='Classic', command=classic_button_action, font=('Arial', 30))
    celebrities_button = tk.Button(root, text='Celebrities', command=celebrities_button_action, font=('Arial', 30))

    welcome_label.place(relx=0.5, rely=0.25, anchor='center')
    classic_button.place(relx=0.5, rely=0.40, anchor='center')
    celebrities_button.place(relx=0.5, rely=0.55, anchor='center')