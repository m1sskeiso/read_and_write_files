# Define a function called write_to_file:
def write_to_file():
    try:
        life_story = [] 
        print("Let's write your life story!\n")  # Print a message to start writing the life story.
        while True:
            line = input("Enter line: ")
            life_story.append(line)
            more_lines = input("\nAre there more lines? (yes/no): ") # Ask the user if there are more lines to add.
            if more_lines.lower() != 'yes':
                break 
        
        # Print a success message indicating that the life story has been written to the file.
        print("\nYour life story has been written to mylife.txt successfully!")
    except Exception as e:
        # Handle any exceptions that might occur during the execution of the code and print an error message.
        print("An error occurred:", e)  
 
write_to_file()
