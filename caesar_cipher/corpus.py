import nltk

from nltk.corpus import words, names

# nltk.download()



nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

def word_check(phrase):

  words_list = words.words()
  names_list = names.words()
  # print(words_list)

  
  word_list_test = phrase.split(' ')

  hits = 0
  num_words = 0

  for word in word_list_test:
      if word.lower() in words_list:
          # print(f'The word {word} is in the list')
          hits += 1
          num_words += 1
      else:
          # print(f'The word {word} is not in the list')
          num_words += 1

  # print(f"{hits/num_words * 100}%")
  return (hits/num_words * 100)



if __name__ == "__main__":
  print(word_check('It was the best of times, it was the worst of times.'))