# Define the input file name
input_file = 'integers.txt'

# Open the input file in read mode
with open(input_file, 'r') as file:
    # Read all lines from the file and convert them to integers
    numbers = [int(num) for num in file.readlines()]

# Create a list containing the square of each even number from the input file
    even_squares = [str(num**2) for num in numbers if num % 2 == 0]

# Create a list containing the cube of each odd number from the input file
    odd_cubes = [str(num**3) for num in numbers if num % 2 != 0]

