'''
Title: Lab 6: Git Encoder
Authors: Noah Adelson and Marco Fernandez
Class: COP3502C
Section: 22282
Description: This program encodes and decodes passwords by incrementing/decrementing each number by 3
'''

def encode(pword): #This function encodes a password by increasing each digit by 3
    eword = ""
    for i in pword:
        n = int(i)
        n += 3
        if n > 9:
            n %= 10
        eword += str(n)

def decode():
    pass

def main():
    password = ""
    encoded_password = ""
    option = 0
    while option != 3:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        try:
            option = int(input("Please enter an option: "))
        except:
            print("Exception Raised, Retry\n")
            continue

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("")
        elif option == 2:
            pass
            #FIXME
        else:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
