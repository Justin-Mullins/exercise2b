"""
Exercise 2b

This takes a series of numbers and returns the average of them.

"""

def average(*numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum / len(numbers)

print(average(*[1, 3, 5]))
print(average(1, 2, 3, 4, 5, 6, 7))