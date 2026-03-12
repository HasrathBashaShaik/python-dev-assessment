# Function 1: Filter even numbers and sort them
def filter_and_sort_evens(numbers):
    evens = []

    for num in numbers:
        if num % 2 == 0:
            evens.append(num)

    evens.sort()
    return evens


# Function 2: Count character frequency (case insensitive)
def count_character_frequency(text):
    frequency = {}

    text = text.lower()

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


# Example test calls
numbers = [5, 2, 9, 8, 1, 4, 6]
print("Even numbers sorted:", filter_and_sort_evens(numbers))

text = "Hello World"
print("Character frequency:", count_character_frequency(text))

python dsa_challenges.py
