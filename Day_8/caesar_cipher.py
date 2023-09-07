alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

directions = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Enter text: ").lower()
shift = int(input("Enter shift number: "))


# def encrypt(plain_text, shift_number):
#     cipher = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         encrypted_value = position + shift_number
#         new_value = alphabet[encrypted_value]
#         cipher += new_value
#     print(f"The encoded text is {cipher}")
#
#
# def decrypt(plain_text, shift_number):
#     cipher = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         decrypted_value = position - shift_number
#         new_value = alphabet[decrypted_value]
#         cipher += new_value
#     print(f"The decoded text is {cipher}")


def cipher(plain_text, shift_number, direction):
    cipher_text = ""
    for letter in plain_text:
        if direction == 'encode':
            position = alphabet.index(letter)
            encrypted_value = position + shift_number
            new_value = alphabet[encrypted_value]
            cipher_text += new_value
        if shift_number > alphabet or shift_number == alphabet:
            remainder = shift_number % 26




        elif direction == 'decode':
            position = alphabet.index(letter)
            encrypted_value = position - shift_number
            new_value = alphabet[encrypted_value]
            cipher_text += new_value
    print(cipher_text)


#
# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     for letter in start_text:
#         position = alphabet.index(letter)
#         if cipher_direction == "decode":
#             shift_amount *= -1
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     print(f"The {cipher_direction}d text is {end_text}")

cipher(plain_text=text, shift_number=shift, direction=directions)
