# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position

plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char.isalpha():  # Only shift alphabetic characters
        encrypted_char = chr(ord(char) + 1)
        if char == 'z':  # Wrap around for lowercase 'z'
            encrypted_char = 'a'
        elif char == 'Z':  # Wrap around for uppercase 'Z'
            encrypted_char = 'A'
    else:
        encrypted_char = char  # Keep non-alphabetic characters

    encrypted_text += encrypted_char

print(f'Original text: {plain_text}')
print(f'Encrypted text: {encrypted_text}')
