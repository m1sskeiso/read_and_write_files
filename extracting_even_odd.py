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

    if not numbers:
        print("Input file is empty.")
    else:
# Append even numbers to even_numbers list and odd numbers to odd_numbers list
        for num in numbers:
            if num % 2 == 0:
                even_numbers.append(str(num))
        else:
            odd_numbers.append(str(num))
            
# Write even numbers to 'even.txt'
with open('even.txt', 'w') as even_file:
    even_file.write('\n'.join(even_numbers))

# Write odd numbers to 'odd.txt'
with open('odd.txt', 'w') as odd_file:
    odd_file.write('\n'.join(odd_numbers))
