# Desc ­> One string is an anagram of another if the second is simply a
# rearrangement of the first. For example, 'heart' and 'earth' are anagrams...
# b. I/P ­> Take 2 Strings as Input such abcd and dcba and Check for Anagrams
# c. O/P ­> The Two Strings are Anagram or not....

def check_anagrams(s1,s2):
    if sorted(s1)==sorted(s2):
        return "Yes,both strings are Anagaram"
    else:
        return "Not an Anagram"


string1 = input("Enter the 1st string: ")

string2 = input("Enter the 2nd string: ")

print(check_anagrams(string1,string2))