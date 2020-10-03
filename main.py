"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64+32)

# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
value_one = 64
value_two = 32
print(value_one + value_two)

# 3.- Make a program that prints a sentence that includes at least 3 variables.
name = "queenie"
color = "blue"
number = "16"
print("I am " + name + " and my favourite colour is " + color + " and I have " + number + " pillows.")

# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."
sentence = "This is my first Python program."
print(len(sentence))

# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"
value_one = 1920*1.1
value_two = 1080*1.1
print("the 10% over-scan 1920 is " + str(value_one) + ", and the 1080 is " + str(value_two))
