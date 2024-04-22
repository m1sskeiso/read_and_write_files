# Define the input file name
input_file = 'numbers.txt'

# Open the input file in read mode
with open(input_file, 'r') as file:
    # Read all lines from the file and convert them to integers
    numbers = [int(num) for num in file.readlines()]

# Check if the list of numbers is empty
if not numbers:
    # If the list is empty, print a message indicating that the input file is empty
    print("The input file is empty.")
else:
    # Create a list containing even numbers from the input file
    even_numbers = [str(num) for num in numbers if num % 2 == 0]
    # Create a list containing odd numbers from the input file
    odd_numbers = [str(num) for num in numbers if num % 2 != 0]

    # Open the output file 'even.txt' in write mode
    with open('even.txt', 'w') as even_file:
        # Write each even number to 'even.txt', separated by newline
        even_file.write('\n'.join(even_numbers))

    # Open the output file 'odd.txt' in write mode
    with open('odd.txt', 'w') as odd_file:
        # Write each odd number to 'odd.txt', separated by newline
        odd_file.write('\n'.join(odd_numbers))
