import tkinter as tk
from tkinter import mainloop
import design
import logic

def main():
    root = tk.Tk()
    root.title("Hangman")
    root.geometry("1200x700")
    word = logic.random_word()
    print(f"Gesuchtes Wort: {word}")
    design.key_board(root, word)

    mainloop()


if __name__ == '__main__':
    main()
