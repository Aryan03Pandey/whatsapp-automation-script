import pywhatkit as kit
import pandas as pd
import pyautogui
import time

df = pd.read_excel('numbers.xlsx', header=None)
phone_numbers = df.iloc[:, 0].tolist()


# Message to be sent
message = "Follow this link to join my WhatsApp group: https://chat.whatsapp.com/JowawAcirad8hpFPTz3CsR"


# Loop through the list of phone numbers and send messages
for phone_number in phone_numbers:
    # Send message
    # kit.sendwhatmsg(phone_number, message, time.localtime().tm_hour, time.localtime().tm_min + 1, 15)
    kit.sendwhatmsg_instantly(phone_number, message, 15)
    
    # Wait for 15 seconds to ensure message typing is complete
    time.sleep(15)
    
    # Move mouse to the text field and click
    pyautogui.click(x=1868, y=984)  # Adjust x and y coordinates as per your WhatsApp Web interface
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w')
    
    # Simulate pressing the 'Enter' key
    # pyautogui.press('enter')
    
    # Wait for 60 seconds before sending the next message
    time.sleep(5)
