"""
a1z26 is an encoding algorithm that encode chars 
to their ascii codes and vice versa for decode.
"""


def encode(plain_text):
    """
    return a list of ascii code of characters
    """
    return [ord(char) for char in plain_text]

def decode(encoded_text):
    """
    convert a list of ascii codes to characters and join them
    """
    return "".join([chr(element) for element in encoded_text])

# Test
print(encode("haji"))
print(decode(encode("haji")))
