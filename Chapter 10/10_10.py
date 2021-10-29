"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 October 2021

Common Words: Visit Project Gutenberg (https://gutenberg.org/ (Links to an external site.)) and find a few texts you’d like to analyze. 
Download the text files for these works, or copy the raw text from your browser into a text file on your computer.

Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. 
This count will be an approximation because of the way split() works.  To get a better idea of what split() is doing, print the list.  
Include an appropriate exception handler for file not found.

You can use the count() method to find out how many times a word appears in a list.   
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
count_common_words(filename, 'the')
