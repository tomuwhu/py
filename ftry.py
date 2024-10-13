"""
A function that counts the occurrences of a specific letter in a given text.

Parameters:
text (str): The text in which to count the occurrences.
l (str): The letter to count in the text.

Returns:
int: The number of occurrences of the letter in the text.
"""
def count_letters(text, l):
    return sum(1 for c in text if c == l)

print(count_letters("cica", "c"))