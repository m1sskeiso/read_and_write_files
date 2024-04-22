# Define the input file name
input_file = 'numbers.txt'

# Initialize lists to store even numbers and odd numbers
even_numbers = []
odd_numbers = []

# Open the input file in read mode
with open(input_file, 'r') as file:
    # Read all lines from the file and convert them to integers
    numbers = [int(num) for num in file.readlines()]
    print("Contents of numbers:", numbers)
    
# Append even numbers to even_numbers list and odd numbers to odd_numbers list
# Write even numbers to 'even.txt'
# Write odd numbers to 'odd.txt'
