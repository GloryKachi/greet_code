import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"The solution is {chosen_word}")

display = []
word_length = len(chosen_word)

lives = 6


end_of_game = False

for _ in range(word_length):
    display += "_"
print(display)


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
        print("You lose")


if "_" not in end_of_game:
    end_of_game = True
    print("You win!")
