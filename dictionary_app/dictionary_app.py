from PyDictionary import PyDictionary
dictionary=PyDictionary()

# word = input("Enter a word you want to search: ")
still_here = 'y'
print('Welcome to my dictionary interface. This is a place you can learn any word in the world.')

while still_here == 'y':
    word = input("Enter a word you want to search: ")
    x = dictionary.meaning(word)
    if x == None:
        still_here = input('This word is incorrect. If you want to try a different word, press "y"')
        word = input("Enter a word you want to search: ")
        x = dictionary.meaning(word)
    word_meaning = x['Noun']
    count = 1
    for i in word_meaning:
        print(f'{count}. {i}')
        count+=1
    still_here = input('Have another word? If so, press y to keep searching.')

# print(dictionary.meaning("alpha"))