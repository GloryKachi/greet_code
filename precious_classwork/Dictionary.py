if __name__ == '__main__':
    paragon = {
        "name_one": "John Doe",
        "name_two": "Peter Dury",
        "name_three": "Jim Beglin",
        "name_four": "Lee Min Hu",
        "name_five": "Kim Jan Di",
        "name_six": "Kim Na Na",
    }
    print(paragon) 

    print(paragon["name_four"])

    paragon["name_four"] = "Kachi"

    paragon.pop("name_six")

    print(paragon)

    paragon.popitem()

    print(paragon)

    val = paragon.get("name_two")

    print(val)
