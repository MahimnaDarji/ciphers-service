def caesar_encoding(plain_text, shift):
    """
    Encodes a plain text using the Caesar cipher.
    :param plain_text: The plain text to encode.
    :param shift: The shift to apply to the plain text.
    :return: The encoded text.
    """
    encoded_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.islower():
                encoded_text += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encoded_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encoded_text += char
    return encoded_text