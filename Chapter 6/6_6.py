"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
16 September 2021

"""

favourite_languages = {
  'Henry': 'Python',
  'James': 'C',
  'Isabelle': 'Ruby',
  'Jack': 'Python',
}

for name, language in favourite_languages.items():
  print(name.title(), "'s favourite language is ", language.title(), ".")

print("\n")

coders = ['Ian', 'Caleb', 'Jose', 'Ken', 'Sally', 'Aaron', 'Wilhelmina']
for coder in coders:
  if coder in favourite_languages.keys():
    print("Thank you for taking the poll, ", coder.title() , "!")
  else:
    print(coder.title(), ", what's your favourite programming language?")
