dictionary = dict()

string = "Check if the word starts with a vowel"


for character in string:
    if character not in dictionary:
        dictionary[character]=1
    else:
        dictionary[character]= dictionary[character]+1
    
print(dictionary)