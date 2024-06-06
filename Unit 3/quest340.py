import re
import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, position):
        self.char = char
        self.position = position

    def __str__(self):
        return f"The username contains an illegal character '{self.char}' at position {self.position}"


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short, it should be at least 3 characters long"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long, it should be at most 16 characters long"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short, it should be at least 8 characters long"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long, it should be at most 40 characters long"


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


def check_input(username, password):
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()
    for i, char in enumerate(username):
        if not (char.isalnum() or char == '_'):
            raise UsernameContainsIllegalCharacter(char, i)

    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()
    if not any(char.isupper() for char in password):
        raise PasswordMissingUppercase()
    if not any(char.islower() for char in password):
        raise PasswordMissingLowercase()
    if not any(char.isdigit() for char in password):
        raise PasswordMissingDigit()
    if not any(char in string.punctuation for char in password):
        raise PasswordMissingSpecial()

    print("OK")


def main():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        try:
            check_input(username, password)
            break
        except Exception as e:
            print(e)


main()