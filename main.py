# Olivia Howse
def encoder(password):
    encoded_password = []
    # get each # separately
    for i in range(len(password)):
        # change to int type
        integer = int(password[i])
        # add 3
        integer += 3
        # append to a new list
        encoded_password.append(integer)
    return encoded_password

# Ivy Li
def decoder(encoded_password):
    decoded_password = []
    # get each number separately
    for i in range(len(encoded_password)):
        # subtract 3
        integer = encoded_password[i] - 3
        # change to string type
        char = str(integer)
        # append to a new list
        decoded_password.append(char)
    return "".join(decoded_password)


def print_list(array):
    for i in array:
        print(i, end='')


if __name__ == '__main__':
    # menu
    while True:
        # print menu
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        # get option
        user_input = int(input('\nPlease enter an option: '))

        # if statements for option
        if user_input == 1:
            print('Please enter your password to encode:', end=' ')
            # store password
            user_password = input()
            print('Your password has been encoded and stored!')
        elif user_input == 2:
            print('The encoded password is', end=' ')
            # encode password
            new_password = encoder(user_password)
            print_list(new_password)
            print(', and the original password is ', end='')
            old_password = decoder(new_password)
            print_list(old_password)
            print('.')
        elif user_input == 3:
            break
