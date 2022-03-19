""" Iterator creates the ability to iterating in custom"""

def iterate(count):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    # Built-in iterator creates a tuple
    iterator = zip(range(count), numbers)

    for position, number in iterator:
        yield number

for num in iterate(5):
    print(num)
