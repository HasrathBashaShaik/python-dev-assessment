# Function to calculate average
def calculate_average(numbers):
    try:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]

        return total / len(numbers)

    except ZeroDivisionError:
        print("Error: Cannot calculate average of an empty list.")
        return None


# Function to get element from list
def get_list_element(my_list, index):
    try:
        return my_list[index]

    except IndexError:
        print("Error: Index is out of range.")
        return None

    except TypeError:
        print("Error: Provided input is not a list or index is invalid.")
        return None


# Example tests
data1 = [10, 20, 30]
data2 = [5, 15]
data3 = []  # empty list

print("Average data1:", calculate_average(data1))
print("Average data2:", calculate_average(data2))
print("Average data3:", calculate_average(data3))


# Testing get_list_element
my_list = [1, 2, 3]

print("Valid index:", get_list_element(my_list, 1))
print("Out of bounds:", get_list_element(my_list, 5))
print("Wrong type:", get_list_element("not_a_list", 1))
