from wordle import WordleGame


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
