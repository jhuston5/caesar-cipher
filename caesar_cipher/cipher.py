try:
  from corpus import word_check

except:
  from caesar_cipher.corpus import word_check

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
  # set the key to be 26
  # iterate 26 times using our decrypt functionality
  # call the cipher function every time on the resulting text
  # Return the highest % phrase
  
  key = 26
  encrypted_text = ''

  for i in range(key):
    
    for char in encrypted:

    # print(f'plain char of {char} not yet shifted by {key}')
      if char.isupper():
        char_idx = ord(char) - ord('A')

        shift = (char_idx + i) % 26 + ord('A')

        new_char = chr(shift)
        encrypted_text += new_char
    
      elif char.islower():
        char_idx = ord(char) - ord('a')

        shift = (char_idx + i) % 26 + ord('a')

        new_char = chr(shift)
        encrypted_text += new_char
      
      else:
        encrypted_text += char
      
    if word_check(encrypted_text) > 50:
      print(encrypted_text)
      return encrypted_text
    
    encrypted_text = ''
    
  if encrypted_text == "":
    return encrypted_text




if __name__ == "__main__":
  # enc1 = encrypt('APPLE', 1)
  # assert enc1 == ('34567')

  # enc2 = encrypt('aP%P5le', 1)
  # assert enc2 == ('34567')

  # dec1 = decrypt('bQQmf', 1)
  # assert dec1 == 'Apple'

  dec2 = crack('It was the best of times it was the worst of times')
  assert dec2 == 'Apple'
