if __name__ == '__main__':
    print("Welcome to treasure island!\nYour mission is to find the treasure!")

    direction = (input("Choose left or right by typing left or right\n")).lower()
    if direction == "right":
        print("oops!You fell into a pit.You lose!")
    else:
        swim_or_wait = input("Choose to swim or wait by typing swim or wait\n").lower()
        if swim_or_wait == "swim":
            print("oops! you got eaten by crocodiles! Game over!")
        else:
            door = input("Choose the door to open by typing yellow,blue or red\n").lower()
            if door == "blue" or door == "red":
                print("oops! you opened the wrong door! Game over!")
            else:
                print("You win darling!")



