# Capital indexes
# Write a function named capital_indexes. 
# The function takes a single parameter, which is a string. 
# Your function should return a list of all the indexes in the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

#import string
cadena = input('Ingrese una palabra que tenga mayusculas y minusculas: ')

def capital_indexes(string):
    capital_indexes_list = []
    contador = 0
    for car in string:
        if car.isupper() == True:
            capital_indexes_list.append(string.index(car,contador,len(string)))
        
        contador +=1
    
    return capital_indexes_list


print(capital_indexes(cadena))

##############################################################################################
##############################################################################################
###############################   S  O  L  U  T  I  O  N  S  #################################
##############################################################################################
##############################################################################################


# naive solution
def capital_indexes(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(s):
        if l in upper:
            result.append(i)
    return result

# shorter version
from string import uppercase
def capital_indexes(s):
    return [i for i in range(len(s)) if s[i] in uppercase]

# you can also use the .isupper() string method.