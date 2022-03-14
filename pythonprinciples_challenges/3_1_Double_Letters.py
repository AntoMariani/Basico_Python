def double_letters(word):
    cont = 0
    while cont < (len(word) - 1) :
        
        if word[cont] == word[cont + 1] :
            return True

        cont +=1
    return False
        

print(double_letters("hello"))


#ejecucion
#primera vuelta : cont  = 0 
# mientras 0 < 3
# si l == e

#segunda vuelta: cont = 1
# mientras 1 < 3
# si e == s

#tercera vuelta: cont = 2
# mientras 2 < 3
# si s == s
# TRUE


##############################################################################################
##############################################################################################
###############################   S  O  L  U  T  I  O  N  S  #################################
##############################################################################################
##############################################################################################

# naive solution
def double_letters(string):
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i+1]
        if letter1 == letter2:
            return True
    return False

# shorter solution
# using a list comprehension, zip, and any
def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])

##The any() function returns True if any element of an iterable is True. If not, it returns False.

# We can use the zip() function to merge our two lists. Here is an example program that will merge this data:

# employee_numbers = [2, 9, 18, 28]
# employee_names = ["Candice", "Ava", "Andrew", "Lucas"]

# zipped_values = zip(employee_names, employee_numbers)
# zipped_list = list(zipped_values)

# print(zipped_list)
# Our zip function returns the following:

# [('Candice', 2), ('Ava', 9), ('Andrew', 18), ('Lucas', 28)]