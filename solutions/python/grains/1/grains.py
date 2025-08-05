def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)


def total():
    sum = 0
    for i in range(64):
        sum = sum + square(i+1)
    return sum
