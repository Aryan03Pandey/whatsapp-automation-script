import pyautogui

# Move your mouse cursor to the button and wait for 5 seconds
print("Move your mouse cursor to the button and wait for 15 seconds...")
print("The coordinates will be printed after 15 seconds.")
pyautogui.sleep(15)

# Get and print the current mouse coordinates
currentMouseX, currentMouseY = pyautogui.position()
print("Button coordinates (X, Y):", currentMouseX, currentMouseY)
