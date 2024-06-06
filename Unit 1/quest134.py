def encrypt_string(string, n):
    """
    Encrypts a string by shifting each character's Unicode code point by 'n'.

    Args:
        string: The string to be encrypted.
        n: The shift amount (positive for encryption, negative for decryption).

    Returns:
        The encrypted or decrypted string.
    """

    return ''.join(chr(ord(char) - n) for char in string)

password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print(encrypt_string(password, -2)
)