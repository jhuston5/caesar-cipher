import nltk

nltk.download()

def encrypt(plain, key):
  # Shift the plain text
  # store the shifted value
  # return the shifted value

  encrypted_text = ''

  for char in plain:
    # print(f'plain char of {char} not yet shifted by {key}')
    encrypted_char = int(char)
    encrypted_char += key
    if encrypted_char > 9:
      encrypted_char = (char + key) % 10
    encrypted_text += str(encrypted_char)
    # print(f'plain char of {encrypted_char} shifted by {key}')
  print(encrypted_text)
  return encrypted_text


def decrypt(encrypted, key):
  return encrypt(encrypted, -key)

def crack(encrypted):
  pass

if __name__ == "__main__":
  enc1 = encrypt('12345', 2)
  assert enc1 == ('34567')

