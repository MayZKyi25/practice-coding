"""
Python fundamentals and interview practice solutions.

This file includes practice problems completed as part of Python review,
coding interview preparation, and LeetCode-style problem solving.

Practice questions:
https://colab.research.google.com/drive/1J_p-AT02T7JyYz0L50J1rPfgfTB6DpQc#scrollTo=EGN9Of_UdKPz
"""


# Problem 1: Find Max and Min
# Description:
# Write functions called find_max and find_min that take a list of numbers
# as input and return the largest/smallest number in the list.
#
# Example:
# Input: numbers = [4, 1, 5, 0, 1, -3]
# Output: 5  for find_max
# Output: -3 for find_min
#
# Logic for find_max:
# 1. Assume the first number is the max.
# 2. Go through each number in the list.
# 3. If the current number is bigger than max_number:
#       update max_number to current number.
# 4. After checking all numbers, return max_number.


def find_max(numbers):
    max_number = numbers[0]

    for current_number in numbers:
        if current_number > max_number:
            max_number = current_number

    return max_number


def find_min(numbers):
    min_number = numbers[0]

    for current_number in numbers:
        if current_number < min_number:
            min_number = current_number

    return min_number


# Problem 2: Count Occurrences of an Element
# Description:
# Write a function called count_element that takes a list and a target element
# as input, and returns how many times the target appears in the list.
#
# Example:
# Input: numbers = [1, 2, 2, 3, 2, 4], target = 2
# Output: 3
#
# Logic:
# 1. Start count at 0.
# 2. Go through each number in the list.
# 3. If the current number is equal to the target:
#       increase count by 1.
# 4. Return count.


def count_element(numbers, target):
    count = 0

    for current_number in numbers:
        if current_number == target:
            count += 1

    return count


def main():
    numbers = [4, 1, 5, 0, 1, -3]

    print(f"Maximum number in the list is: {find_max(numbers)}")
    print(f"Minimum number in the list is: {find_min(numbers)}")

    values = [1, 2, 2, 3, 2, 4]
    target = 2

    print(f"Count occurrence of element {target} is {count_element(values, target)} times.")


if __name__ == "__main__":
    main()

