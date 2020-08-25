MIN_LENGTH = 6

def main():
    password = input("Enter a password no less than {} characters: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        password = input("Enter a password no less than {} characters: ".format(MIN_LENGTH))
    print("*" * len(password))

main()
