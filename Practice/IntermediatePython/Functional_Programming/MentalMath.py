"""
Let’s practice using list comprehensions to create a list of even 
numbers from the following list of integers:
"""
numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]

"""
Create a list comprehension that filters the even numbers.
Print the original range and the list of even numbers.

Original Numbers: [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
Even Numbers: [10, 82, 36, 46, 92, 48]
"""

print("Original Number:", numbers,"\nEven Number:", [i for i in numbers if i % 2 == 0])