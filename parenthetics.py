# this function will return a number depending on the balance of parentheses


def is_balanced(text):
    count = 0
    # loops through inputted text
    for char in text:
        # adds one to count if there is an open paren
        if char == '(':
            count += 1
        # subtracts one if there is a closed paren
        if char == ')':
            count -= 1
        # if there is a closed without an open attached, return
        if count == -1:
            return count
    # if there is more than one open paren, just return one
    if count > 0:
        return 1
    # otherwise return the count
    return count
