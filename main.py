import tkinter as tk
import start_screen
import logic

def main():
    root = tk.Tk()
    root.title("Hangman")
    root.geometry("1200x700")
    root.configure(bg="#41423d")


    word = logic.random_word()
    print(f"Gesuchtes Wort: {word}")
    start_screen.start_screen(root)
    root.mainloop()


if __name__ == '__main__':
    main()
