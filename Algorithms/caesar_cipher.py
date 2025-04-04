from string import ascii_lowercase


def encrypt(text: str, shift: int) -> str:
    encrypted_text = ""
    for ch in text:
        if ch in ascii_lowercase:
            index = (ascii_lowercase.index(ch) + shift) % 26
            encrypted_text += ascii_lowercase[index + shift]
        else:
            encrypted_text += ch

    return encrypted_text


def decrypt(text, shift):
    shift = shift * -1
    return encrypt(text, shift)


text = "sample"
shift = 2

encrypted_text = encrypt(text, 2)
print(encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print(decrypted_text)
