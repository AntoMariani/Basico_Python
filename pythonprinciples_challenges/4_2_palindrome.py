# Palindrome
# A string is a palindrome when it is the same when read backwards.

# For example, the string "bob" is a palindrome. 
# So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".

# Write a function named palindrome that takes a single string as its parameter.
#  Your function should return True if the string is a palindrome, and False otherwise.

def palindrome(word):
    return word == ''.join(reversed(list(word)))

print(palindrome("neuquen"))

##############################################################################################
##############################################################################################
###############################   S  O  L  U  T  I  O  N  S  #################################
##############################################################################################
##############################################################################################

# check if reversing the string gives the same string.
def palindrome(string):
    return string == string[::-1]

# Slice notation "[a:b:c]" means "count in increments of c starting at a inclusive, up to b exclusive". If c is negative you count backwards, if omitted it is 1. If a is omitted then you start as far as possible in the direction you're counting from (so that's the start if c is positive and the end if negative). If b is omitted then you end as far as possible in the direction you're counting to (so that's the end if c is positive and the start if negative). If a or b is negative it's an offset from the end (-1 being the last character) instead of the start.

# OK, so string[0::-1] is one character, it says "count backwards from index 0 as far as you can". As far as it can is the start of the string.

# string[0:len(string):-1] or for that matter string[0:anything:-1] is subtly different. It's empty for the same reason that string[1:0] is empty. The designated end of the slice cannot be reached from the start. You can think of this as the slice having ended "before" it began (hence is empty), or you can think of the end point being automatically adjusted to be equal to the start point (hence the slice is empty).

# string[:len(string):-1] means "count backwards from the end up to but not including index len(string)". That index can't be reached, so the slice is empty.

# You didn't try string[:0:-1], but that means "count backwards from the end up to but not including index 0". So that's all except the first character, reversed. [:0:-1] is to [::-1] as [0:len(string)-1] is to [:]. In both cases the excluded end of the slice is the index that would have been the included last character of the slice with the end omitted.

# You also didn't try string[-1::-1], which is the same as string[::-1] because -1 means the last character of the string.