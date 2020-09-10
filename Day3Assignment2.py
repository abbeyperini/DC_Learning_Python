def check_palindrome():
    palindrome = input("Type in a word to see if it's a palindrome! ")
    letters = []
    letters_reverse = []

    for i in range(0, len(palindrome)):
        letters.append(palindrome[i])

    for i in range((len(palindrome) - 1), -1, -1):
        letters_reverse.append(palindrome[i])

    if letters == letters_reverse:
        print("It's a palindrome!")
    else:
        print("Not a palindrome.")

check_palindrome()