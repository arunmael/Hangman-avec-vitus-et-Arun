import tkinter as tk
import design
import logic

def main():
    root = tk.Tk()
    root.title("Hangman")
    root.geometry("700x700")
    root.configure(bg="#41423d")


    word = logic.random_word()
    print(f"Gesuchtes Wort: {word}")
    design.key_board(word, root)
    design.draw_hangman(root)
    root.mainloop()


if __name__ == '__main__':
    main()
