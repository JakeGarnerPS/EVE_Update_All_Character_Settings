import os
import re
import shutil

# Prompt the user for the folder path
folder_path = input("Enter the folder path: ")

# Prompt the user for charID and userID
charID = input("Enter the charID: ")
userID = input("Enter the userID: ")

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
mainCharPath = os.path.join(folder_path, 'core_char_' + charID + '.dat')
mainUserPath = os.path.join(folder_path, 'core_user_' + userID + '.dat')

# Iterate through the matched files and read each one
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)

    # Ignore main chars files
    if file_path != mainCharPath and file_path != mainUserPath:
    
        # Check if the path is a file (not a directory)
        if os.path.isfile(file_path):                    
            #print(f"File name {file_name}")

            if 'core_char' in file_name:              
                
                # Rename old file with 'old' tag 
                os.rename(file_path, os.path.join(folder_path, 'old_' + file_name))

                # Copy and rename 'core_char' files  
                shutil.copy(mainCharPath, file_path)
               
                print(f"File {file_name} updated")

                # Remove old file
                os.remove(os.path.join(folder_path, 'old_' + file_name))

             # Check if the file name contains 'core_user'
            elif 'core_user' in file_name:

                # Rename old file with 'old' tag 
                os.rename(file_path, os.path.join(folder_path, 'old_' + file_name))

                # Copy and rename 'core_char' files  
                shutil.copy(mainUserPath, file_path)              
                
                print(f"File {file_name} updated")
                
                # Remove old file
                os.remove(os.path.join(folder_path, 'old_' + file_name))

# Keep console open for user to view changes 
input("Press any button to close")