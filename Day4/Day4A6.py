# HARD Assignment - Write a program to display a pyramid with asterisks

def pyramid():

    spaces = "        "
    asterisks = "*"

    while len(asterisks) <= 17:
        print(spaces + asterisks + spaces)
        spaces = spaces[:-1]
        asterisks += "**"

pyramid()
