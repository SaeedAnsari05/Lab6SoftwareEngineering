def main():
    menu_continue = True

    while menu_continue == True:

        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option: "))
        if option == 1:
            password_to_encode = input("Please enter your password to encode: ")
            encoder(password_to_encode)
            print("Your new password has been created and stored!")
        if option == 2:
            decoder(password_to_decode)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}')
        if option == 3:
            menu_continue = False

def encoder(password_to_encode):
    original_password = password_to_encode
    password_to_encode = list(str(password_to_encode))
    encoded_password = ""

    for i in range(len(password_to_encode)):
        encoded_password += (str(int(password_to_encode[i]) + 3))

    return encoded_password

if __name__ == "__main__":
    main()

def decoder(password_to_decode):
    original_password = password_to_decode
    password_to_decode = list(str(password_to_decode))
    decoded_password = ""

    for i in range(len(password_to_decode)):
        decoded_password += (str(int(password_to_decode[i]) - 3))

    return decoded_password

