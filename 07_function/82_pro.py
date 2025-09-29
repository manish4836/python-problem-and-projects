def is_polydrome(name):
    rev = ""
    for ch in name:
        rev = ch + rev

    if name == rev:
        print("the string is polydrome.")
    else :
        print("the string is not polydrome.")

is_polydrome("madam")


#this is the another method

def is_palindrome(word):
    # A string slice [::-1] creates a reversed copy of the string.
    reversed_word = word[::-1]
    
    if word == reversed_word:
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")

is_palindrome("madam")
# Output: 'madam' is a palindrome.

is_palindrome("hello")
# Output: 'hello' is not a palindrome.