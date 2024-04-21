import csv

with open('students_gwa.csv', 'r') as file:
    reader = csv.reader(file)

    for line in reader:
        print(line)