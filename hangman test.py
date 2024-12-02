import tkinter as tk
from random import choice

class HangmanGame:
    def __init__(self):
        self.start_window = (tk.Tk)()
        self.start_window.title("Hangman Game")

        self.start_label = tk.Label(self.start_window, text="Welcome to Hangman!", font=("Arial", 24))
        self.start_label.pack()

        self.start_button = tk.Button(self.start_window, text="Start Game", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        self.start_window.destroy()

        self.game_window = (tk.Tk)()
        self.game_window.title("Hangman Game")

        self.word_list = ["apple", "banana", "cherry", "skate", "basketball"]
        self.word = choice(self.word_list)
        self.guessed_word = ["_"] * len(self.word)
        self.guessed_letters = []
        self.tries = 6

        self.word_label = tk.Label(self.game_window, text=" ".join(self.guessed_word), font=("Arial", 24))
        self.word_label.pack()

        self.guess_entry = tk.Entry(self.game_window, font=("Arial", 24))
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.game_window, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.result_label = tk.Label(self.game_window, text="", font=("Arial", 24))
        self.result_label.pack()

        self.game_window.mainloop()

    def check_guess(self):
        guess = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1:
            self.result_label['text'] = "Please guess one letter at a time."
            return

        if guess in self.guessed_letters:
            self.result_label['text'] = "You already guessed this letter."
            return

        self.guessed_letters.append(guess)

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed_word[i] = guess
            self.word_label['text'] = " ".join(self.guessed_word)
        else:
            self.tries -= 1
            self.result_label['text'] = f"Incorrect guess. You have {self.tries} tries left."

        if "_" not in self.guessed_word:
            self.result_label['text'] = "Congratulations, you won!"
            self.guess_button['state'] = tk.DISABLED
        elif self.tries == 0:
            self.result_label['text'] = f"Game over. The word was {self.word}."
            self.guess_button['state'] = tk.DISABLED

    def run(self):
        self.start_window.mainloop()

if __name__ == "__main__":
    game = HangmanGame()
    game.run()
