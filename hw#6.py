def is_palindrome(word):
    return word == word[::-1]

user_word = input("Nikita")
if is_palindrome(user_word):
    print("паліндром")
else:
    print("не паліндром.")