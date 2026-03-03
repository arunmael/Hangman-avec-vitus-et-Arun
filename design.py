"""
This File is for the desing of the game
"""
import tkinter as tk

root = tk.Tk()
root.title("Hangman")
root.geometry("400x300")


#Test
button = tk.Button(root, text="A")
button.pack()


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