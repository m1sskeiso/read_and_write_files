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

    # Open the output file 'double.txt' in write mode
    with open('double.txt', 'w') as double_file:
        # Write each even square to 'double.txt', separated by newline
        double_file.write('\n'.join(even_squares))

    # Open the output file 'triple.txt' in write mode
    with open('triple.txt', 'w') as triple_file:
        # Write each odd cube to 'triple.txt', separated by newline
        triple_file.write('\n'.join(odd_cubes))



