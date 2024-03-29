# EVE_Update_All_Character_Settings

## Overview

This script streamlines the process of updating all your characters' settings by aligning them with your main (selected) character's configurations. It's a quick solution for efficiently applying uniform settings across multiple characters, char, and user files.

**Created by:** JakeGarnerPS  
**In-game character:** Jeff Fastbender

While this script was crafted for enjoyment, please be aware that it may exhibit some quirks. If you encounter any issues, feel free to contact me in-game or through [GitHub](https://github.com).

**Donations are appreciated but not mandatory.**

## Instructions

Follow these steps to ensure the proper functioning of the script:

1. **Download**: Obtain the `main.dist.zip` folder, which contains the executable (.exe) file. Extract the folder to a where ever you want it.

   **Important**: Create a backup of the files or folder you intend to modify.

2. **Backup Existing Files**:
   - Navigate to `C:\Users\USERNAME\AppData\Local\CCP\EVE\c_ccp_eve_online_tq_tranquility`.
   - Create a copy of the folder you wish to modify.

3. **Launch EVE Client**:
   - Open the Eve client.
   - Log in with the character whose settings you want to replicate.
   - After logging in, close the game.

4. **Access Settings Folder**:
   - Open the copied settings folder.
   - Identify the two most recent files: `core_char` and `core_user`. These represent your character IDs.
   - Note down both numbers, distinguishing between the user and character IDs, and also record the folder path.

5. **Run the Script**:
   - Execute the `.exe` file.
   - It will prompt you for the folder path; paste it in and press 'Enter'.
   - Provide the Character ID (from `core_char` file) when prompted and press 'Enter'.
   - Provide the User ID (from `core_user` file), paste the number, and press 'Enter'.

6. **Confirmation**:
   - The process is complete, and your accounts should be updated.
   - Verify by either logging in and checking or examining the Date Modified time (it should reflect the time you ran the .exe).
