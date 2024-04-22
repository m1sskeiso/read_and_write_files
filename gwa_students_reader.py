# Define the input file name
input_file = 'students_data.txt'

# Initialize variables to store the student names and GWAs
student_gwa = {}

# Open the input file in read mode using the input_file variable
with open(input_file, 'r') as file:
    # Process each line in the file
    for line in file:
        # Split the line into name and GWA based on comma
        data = line.strip().split(',')
        if len(data) == 2:
            name = data[0].strip()
            gwa = data[1].strip()