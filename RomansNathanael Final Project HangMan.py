#importing tkinter and the random module
import tkinter as tk
from random import choice

#creating class HangManGame
class HangmanGame:
    #initializing attributes for HangManGame class
    def __init__(self):
        self.start_window = (tk.Tk)() #creating window
        self.start_window.geometry("1920x1080") #winddow size
        self.start_window.title("Hangman Game") #window title



        #creating start label, defining its window, the text, font, and size
        self.start_label = tk.Label(self.start_window, text="Welcome to Hangman!", font=("Times New Roman", 24))
        self.start_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)#start label placement

        #creating start button, definging its window, the text, font, and size
        self.start_button = tk.Button(self.start_window, text="Start Game", command=self.start_game)
        self.start_button.place(relx=0.5, rely=0.55, anchor=tk.CENTER)#start button placement



    #creating function start__game
    def start_game(self):
        self.start_window.destroy() #deletes start window
        self.game_window = (tk.Tk)() #creates game window
        self.game_window.geometry("1920x1080") #define window size
        self.game_window.title("Hangman Game") #window title



        self.word_list = ["apple", "banana", "cherry", "skate", "basketball"] #list of words
        self.word = choice(self.word_list) #selects a random word from the list
        self.guessed_word = ["_"] * len(self.word) #gets the amount of characters in a word to display the correct amount of dashes
        self.guessed_letters = [] #creates an empty list to store letters guessed by the player
        self.tries = 6  #the player has 6 wrong guesses



        #Creates a frame for the player to guess a letter
        self.guess_frame = tk.Frame(self.game_window)
        self.guess_frame.place(relx=0.5, rely=0.2, anchor=tk.CENTER) #position of frame


        #creates a label in the guess frame to display the current state of the word being guessed, defines font and size
        self.word_label = tk.Label(self.guess_frame, text=" ".join(self.guessed_word), font=("Times New Roman", 24))
        self.word_label.pack() #adds label to frame


        #creates input box for entering letters, defines font and size
        self.guess_entry = tk.Entry(self.guess_frame, font=("Times New Roman", 24))
        self.guess_entry.pack()#adds input box to frame

        #creates guess button
        self.guess_button = tk.Button(self.guess_frame, text="Guess", command=self.check_guess)
        self.guess_button.pack()#adds guess button to frame

        #creates result label
        self.result_label = tk.Label(self.guess_frame, text="", font=("Times New Roman", 24))
        self.result_label.pack()#adds result label to frame

        #creates a canvas for drawing the hangman figure
        self.canvas = tk.Canvas(self.game_window, width=400, height=400)#canvas window and size
        self.canvas.place(relx=0.5, rely=0.6, anchor=tk.CENTER)#canvas position

        self.draw_hangman(self.tries)#calls draw_hangman based on remaining tries

        self.game_window.mainloop()#starts the tkinter event loop



    #creates a function draw_hangman
    def draw_hangman(self, tries):
        
        #insures at the start of each game the hangman is cleared and ready for a new game
        self.canvas.delete("all")
        
        #Draw gallows, size and position
        self.canvas.create_line(100, 350, 300, 350, width=5)
        self.canvas.create_line(200, 350, 200, 100, width=5)
        self.canvas.create_line(200, 100, 300, 100, width=5)

        
        #if the number of tries is less than or equal to 5, it draws the head
        #if less than 4, it draws the body, and so on
        if tries <= 5:
            self.canvas.create_oval(270, 120, 330, 180, width=5)  #Head
        if tries <= 4:
            self.canvas.create_line(300, 180, 300, 220, width=5)  #Body
        if tries <= 3:
            self.canvas.create_line(300, 200, 270, 220, width=5)  #Left arm
        if tries <= 2:
            self.canvas.create_line(300, 200, 330, 220, width=5)  #Right arm
        if tries <= 1:
            self.canvas.create_line(300, 220, 270, 250, width=5)  #Left leg
        if tries <= 0:
            self.canvas.create_line(300, 220, 330, 250, width=5)  #Right leg

    #creating a function check guess
    def check_guess(self):

        #retrieves user input from the guess entry and then clears the field
        guess = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)

        #if the guess entry is anything other than one, promt user to guess one letter
        if len(guess) != 1:
            self.result_label['text'] = "Please guess one letter at a time."
            return

        #if guess is in the already guessed list, promt user theyve already guessed that letter
        if guess in self.guessed_letters:
            self.result_label['text'] = "You already guessed this letter."
            return

        #adds guess to guessed letters list
        self.guessed_letters.append(guess)

        #checks if the guess is in the word
        if guess in self.word:
            for i, letter in enumerate(self.word):#iterates through each letter in the word

                #updates guessed word list by added the correct guess at the correct index
                if letter == guess:
                    self.guessed_word[i] = guess
                    
            self.word_label['text'] = " ".join(self.guessed_word)#updates word label
        else:
            self.tries -= 1#decriments tries
            self.result_label['text'] = f"Incorrect guess. You have {self.tries} tries left." #displays warning to user
            self.draw_hangman(self.tries) #calls draw hang man function

            
        if "_" not in self.guessed_word:#if there are no more empty guesses
            self.result_label['text'] = "Congratulations, you won!"#diplay congratulations to user
            self.guess_button['state'] = tk.DISABLED #disables guess button

            
        elif self.tries == 0: #if tries falls to 0
            self.result_label['text'] = f"Game over. The word was {self.word}."#promts user game over and displays correct word
            self.guess_button['state'] = tk.DISABLED #disables guess button
    #creates run function
    def run(self):
        self.start_window.mainloop()#adds the main loop to the run function

        
#initializes and run the application
if __name__ == "__main__":
    game = HangmanGame()
    game.run()
