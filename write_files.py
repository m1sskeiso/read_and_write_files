# Define a function called write_to_file:
def write_to_file():
        life_story = [] 
        print("Let's write your life story!\n")  # Print a message to start writing the life story.
        while True:
            line = input("Enter line: ")
            life_story.append(line)
            more_lines = input("\nAre there more lines? (yes/no): ") # Ask the user if there are more lines to add.
            if more_lines.lower() != 'yes':
                break 

write_to_file()
