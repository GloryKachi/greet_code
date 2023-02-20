import random

word_list = ["aardvark", "baboon", "carmel"]

# chosen_word = word_list
# user_input = input("Guess a letter to save Mr HangMan: ")

# for word in chosen_word:
# for letter in word:
# guess = user_input.lower()
# if guess == letter:
# print("right")
# else:
# print("wrong")
# for letter in chosen_word:
#   if guess == letter:
#      print([guess])
# else:
#    print(['_'])

chosen_word = random.choice(word_list)
print(chosen_word)
# user_input = input("Guess a letter to save Mr HangMan: ").lower()

current_word = len(chosen_word)

display = []

end_of_game = False
while not end_of_game:
    user_input = input("Guess a letter to save Mr HangMan: ").lower()
    for each_letter in range(current_word):
        display += "_"
    print(display)

    for each_letter in range(current_word):
        letter = chosen_word[each_letter]
        if user_input == letter:
            display[each_letter] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
