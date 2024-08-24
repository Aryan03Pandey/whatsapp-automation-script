import pywhatkit as kit
# kit.start_server()
# import time

# List of phone numbers along with the country code (e.g., +123456789)
# phone_numbers = ["+1234567890", "+1987654321", "+1122334455", ...]  # Add your phone numbers here

phone_number = "+918595703711"

# Message to be sent
message = "Follow this link to join my WhatsApp group: https://chat.whatsapp.com/JowawAcirad8hpFPTz3CsR"

# Loop through the list of phone numbers and send messages
# for phone_number in phone_numbers:
    # Send message
kit.sendwhatmsg_instantly(phone_number, message, 15)
    # Wait for 60 seconds before sending the next message
# time.sleep(60)
