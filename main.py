# Jason Von Holten



def encoder(password):
    encoded_password = ""
    for element in password:
        element = int(element) + 3
        if element == 10:
            element = 0
        if element == 11:
            element = 1
        if element == 12:
            element = 2
        encoded_password += str(element)
    return encoded_password

def decoder(encoded_password):
    decoded_password = ""
    for element in encoded_password:
        val = int(element) - 3
        if val <= 0:
            val += 10
        decoded_password += str(val)
    return decoded_password


if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")


        option = input("Please enter an option: ")


        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")


        if option == "2":
            print(f"The encoded password is {encoded_password}, and the original password is {decoder(encoded_password)}")
            pass


        if option == "3":
            break


