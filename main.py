import os
import re
import shutil

def update_file(folder_path, char_id, user_id):
# Define regular expression patterns to match 'core_char_' and 'core_user_' followed by any number
    char_pattern = re.compile(r'core_char_\d+\.dat')
    user_pattern = re.compile(r'core_user_\d+\.dat')

    # List all files in the folder
    file_list = os.listdir(folder_path)

    # Iterate through the files and filter based on patterns
    char_files = [file_name for file_name in file_list if char_pattern.match(file_name)]
    user_files = [file_name for file_name in file_list if user_pattern.match(file_name)]

    # Combine the lists of matched files
    file_list = char_files + user_files

    # Create file paths for main chars files
    main_char_path = os.path.join(folder_path, f'core_char_{char_id}.dat')
    main_user_path = os.path.join(folder_path, f'core_user_{user_id}.dat')

    # Iterate through the files and filter based on patterns
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)

        # Ignore main chars files
        if file_path != main_char_path and file_path != main_user_path:

            # Check if the path is a file (not a directory)
            if os.path.isfile(file_path):
                # Rename old file with 'old' tag 
                os.rename(file_path, os.path.join(folder_path, f'old_{file_name}'))

                # Copy and rename 'core_char' or 'core_user' files  
                main_file_path = main_char_path if 'core_char' in file_name else main_user_path
                shutil.copy(main_file_path, file_path)

                print(f"File {file_name} updated")

                # Remove old file
                os.remove(os.path.join(folder_path, f'old_{file_name}'))

# Prompt the user for the folder path
folder_path = input("Enter the folder path: ")
char_id = input("Enter the charID: ")
user_id = input("Enter the userID: ")

# Call the function
update_file(folder_path, char_id, user_id)

# Keep console open for user to view changes 
input("Press any button to close")