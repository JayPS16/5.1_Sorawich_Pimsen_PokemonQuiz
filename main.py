import random

from cards import CARDS
from quiz import check_answer, is_valid_input, score_summary


def main():
    cards = list(CARDS.items())
    random.shuffle(cards)
    correct = 0

    for pokemon, pokemon_type in cards:
        while True:
            answer = input(f"What is the type of {pokemon}? ")
            if is_valid_input(answer):
                break
            print("Please enter an answer.")

        if check_answer(answer, pokemon_type):
            correct += 1
            print("Correct!")
        else:
            print(f"Incorrect. The answer is {pokemon_type}.")

    print(f"Final score: {score_summary(correct, len(cards))}")


if __name__ == "__main__":
    main()
