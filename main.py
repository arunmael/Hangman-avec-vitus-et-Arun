import tkinter as tk
import start_screen
import logic
mode = 'classic'
random_word = ''
random_celebritie = ''

def main():
    root = tk.Tk()
    root.title("Hangman")
    root.geometry("1200x700")
    root.configure(bg="#41423d")

    word = logic.random_word()
    celb = logic.celebrities_word()
    print(f"Gesuchtes Wort: {word}")
    print(f"Gesuchte Wort: {celb}")
    start_screen.start_screen(root, word, celb)
    root.mainloop()


if __name__ == '__main__':
    main()
