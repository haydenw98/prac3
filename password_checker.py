MIN_LENGTH = 6

def main():
    password = password_get()
    password_print(password)


def password_print(password):
    print("*" * len(password))


def password_get():
    password = input("Enter a password no less than {} characters: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        password = input("Enter a password no less than {} characters: ".format(MIN_LENGTH))
    return password

main()
