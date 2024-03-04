from colorama import init
from termcolor import colored
from random_words import RandomWords
import re
import enchant


class WordleGame:
    def __init__(self):
        self.word = self.generate_word()
        print(self.word)
        self.guesses = []
        self.game_won = False

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
        init()
        for r in range(rows):
            correct = 0
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
                            correct += 1
                        else:
                            print(colored(letter_space, "white", "on_yellow"), end="")
                    # If letter is not in the word
                    else:
                        print(colored(letter_space, "white", "on_dark_grey"), end="")
            print("")
            # Check if user correctly guessed all 5 letters
            if correct == 5:
                self.game_won = True

    def is_game_won(self) -> bool:
        return self.game_won

    def get_user_input(self) -> None:
        while True:
            word = input("English word: ")
            if self.__is_word_len5(word):
                self.guesses.append(word)
                break
            else:
                print(
                    "ERROR. Enter 5 letter English word that contains only alphabetical letters. "
                )

    def __is_english_word(self, word: str) -> bool:
        english_dict = enchant.Dict("en_US")
        return english_dict.check(word)

    def __is_word_len5(self, word: str) -> bool:
        # Check if word is composed of 5 alphabetical chars
        if re.search(r"^[A-Za-z]{5}$", word) == None:
            return False
        # Check if word is legit english word
        if not self.__is_english_word(word.lower()):
            return False
        return True

    def print_result(self) -> None:
        if self.game_won == False:
            print(f"You Lost! Word to guess was '{self.word}'")
        elif self.game_won == True:
            print(f"You Win! Word to guess was '{self.word}'")


def main():
    game = WordleGame()
    game.show_grid()

    for _ in range(6):
        game.get_user_input()
        game.show_grid()
        if game.is_game_won():
            break

    game.print_result()


if __name__ == "__main__":
    main()
