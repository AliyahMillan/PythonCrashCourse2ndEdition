"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 October 2021

Common Words II: Starting with your program from 10-10, modify it such that it can take a word from the user and search the book for the number of occurrences of that word.
"""

def count_common_words(filename, word): #324 is 'the' goal
  try:
    with open(filename, encoding='utf-8') as f:
      contents = f.read()
  except FileNotFoundError:
    pass
  else:
    word_count = contents.lower().count(word)
    msg = f"'{word}' appears in {filename} a total of {word_count} times."
    print(msg)

filename = 'HeyDiddleDiddleTXT.txt'
blue = input("Which word would you like to search for in " + filename + "?\n")

count_common_words(filename, blue)

#the: 324 times
#to: 90
#blue: 0


##################################See HeyDiddleDiddleTXT.txt
