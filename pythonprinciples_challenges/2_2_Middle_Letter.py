# Middle letter
# Write a function named mid that takes a word as its parameter. 
# Your function should extract and return the middle letter.
# If there is no middle letter, your function should return the empty word.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(word):
    if len(word) % 2 == 0:
        middleLetter = ''
    elif len(word) % 2 != 0:
        middleLetterIndex = int((len(word) / 2))
        print(middleLetterIndex)
        middleLetter = word[middleLetterIndex]
    return middleLetter

print(mid("perro"))

##############################################################################################
##############################################################################################
###############################   S  O  L  U  T  I  O  N  S  #################################
##############################################################################################
##############################################################################################

# this approach uses // which is integer division in Python 3
# alternatively, use / and int() in combination.
def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]