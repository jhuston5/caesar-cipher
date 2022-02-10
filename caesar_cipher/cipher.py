

def encrypt(plain, key):
  # Shift the plain text
  # store the shifted value
  # return the shifted value

  encrypted_text = ''

  for char in plain:
    # print(f'plain char of {char} not yet shifted by {key}')
    if char.isupper():
      char_idx = ord(char) - ord('A')

      shift = (char_idx + key) % 26 + ord('A')

      new_char = chr(shift)
      encrypted_text += new_char
   
    elif char.islower():
      char_idx = ord(char) - ord('a')

      shift = (char_idx + key) % 26 + ord('a')

      new_char = chr(shift)
      encrypted_text += new_char
    
    else:
      encrypted_text += char

    
  print(encrypted_text)
  return encrypted_text


def decrypt(encrypted, key):
  return encrypt(encrypted, -key)

def crack(encrypted):
  # set the key to be 
  pass

if __name__ == "__main__":
  # enc1 = encrypt('APPLE', 1)
  # assert enc1 == ('34567')

  # enc2 = encrypt('aP%P5le', 1)
  # assert enc2 == ('34567')

  dec1 = decrypt('bQ%  Q5mf', 1)
  assert dec1 == 'Apple'
