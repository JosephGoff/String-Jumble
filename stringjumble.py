"""
stringjumble.py
Author: Joseph Goff
Credit: Billy Bender

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
string = input("Please enter a string of text (the bigger the better): ")
print("You entered " +'"' + string +'"'+ ". Now jumble it:")
word= ""
words = []
wordsbackwards=[]
for x in string:
    if x == " ":
        words.append(word)
        word = ""
    else:
        word = word + x
words.append(word)
for m in range(len(words)-1,-1,-1):
    wordsbackwards.append(words[m])
reverse= "" 
for x in string:
    reverse = x + reverse
print(reverse)
print(' '.join(wordsbackwards))
characterreverse = words
for a in range(0, len(characterreverse), 1):
    wordreverse = ""
    for b in (characterreverse[a]):
        wordreverse = b + wordreverse
    characterreverse[a] = wordreverse
print(' '.join(characterreverse))