from colorama import init
from termcolor import colored
from random_words import RandomWords


class WordleGame:

    def __init__(self):
        self.word = self.generate_word()
        print(self.word)
        self.guesses = []

    # Generate a random word that has a lenght of 5 chars
    def generate_word(self) -> str:
        rw = RandomWords()
        while True:
            word = rw.random_word(min_letter_count=5)
            if len(word) != 5:
                continue
            return word

    def show_grid(self) -> None:
        columns = 5
        rows = 6

        for r in range(rows):
            for c in range(columns):
                # Check if user made a guess
                try:
                    word = self.guesses[r]
                    letter = word[c]
                    letter_space = " " + letter + " "
                # If user didnt made a guess print "-"
                except IndexError:
                    print(colored(" - ", "white", "on_dark_grey"), end="")
                else:
                    # Check if letter is in the word
                    if letter in self.word:
                        # Check if letter in in the same position as the word in guess
                        if letter == self.word[c]:
                            print(colored(letter_space, "white", "on_green"), end="")
                        else:
                            print(colored(letter_space, "white", "on_yellow"), end="")
                    # If letter is not in the word
                    else:
                        print(colored(" - ", "white", "on_dark_grey"), end="")
            print("")

    def get_user_input(self) -> str:
        word = input(": ")
        self.guesses.append(word)
        return word

    def guess_word(self) -> None: ...


def main():
    game = WordleGame()
    game.show_grid()


if __name__ == "__main__":
    main()
