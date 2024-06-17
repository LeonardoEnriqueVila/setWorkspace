# Set Workspace

This project is a basic script that i use to open a folder in vs code in a very fast way. 

## Description

The script uses a simple dialog from tkinter where the user can prompt the folder name that they want to open in VS Code. The name does not need to match exactly; the script can find the folder even if it doesn't match perfectly. 
It is important to note that this works in my own environment, but it may not work in different environments. 
It is included here as part of my learning process. I encourage potential employers to check out my other projects which are more interesting.

## Modules used

- **os**: Provides functions to interact with the operating system, such as file and directory manipulation.
- **tkinter**: Used for creating graphical user interfaces (GUIs). In this script, it is used to create a dialog box for user input.
- **subprocess**: Allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. In this script, it is used to open the folder in VS Code.
- **difflib**: Provides classes and functions for comparing sequences. In this script, it is used to find the closest matching folder name entered by the user.