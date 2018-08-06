'''
 Exercise 3:
 Given a paragraph of text,
 1. count the number of times each character occurs in the text,
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''
import operator

def count_char(text):
    text_list=list(text)
    letter_dict= {}
    for x in text_list:
        if x in letter_dict:
            letter_dict[x] +=1
        else:
            letter_dict[x]= 1
    print (letter_dict)

def count_char_insensitive(text):
    text= text.lower()
    text_list=list(text)
    letter_dict= {}
    for x in text_list:
        if x in letter_dict:
            letter_dict[x] +=1
        else:
            letter_dict[x]= 1
    print (letter_dict)

# bonus task:
def count_char_ordered(text):
    text_list=list(text)
    letter_dict= {}
    for x in text_list:
        if x in letter_dict:
            letter_dict[x] +=1
        else:
            letter_dict[x]= 1
    '''sorted_x = sorted(letter_dict.items(), key= operator.itemgetter(1),reverse = True)
    print(sorted_x)'''
    '''new_dict = sorted(letter_dict, key=letter_dict.get, reverse=True)
    print(new_dict)
    new_dict1 =sorted(letter_dict.items(), key=lambda x: x[1])
    print(new_dict1)'''
    new_dict = {}
    new_dict2 =sorted(letter_dict.values(), reverse = True)
    for x in new_dict2:
        if x in letter_dict:
            letter_dict[x] +=1
        else:
            letter_dict[x]= 1
    print(new_dict2)
    # add your code here

text1 = 'I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy' # Robert Bolano
text2 = 'HellO, WorLd!'

# testing exercise 2
count_char(text1)
count_char_insensitive(text1)
count_char_ordered(text1)
