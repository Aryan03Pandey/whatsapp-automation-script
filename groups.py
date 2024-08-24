from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Read phone numbers from Excel sheet
df = pd.read_excel('phones.xlsx', header=None)
phone_numbers = df.iloc[:, 0].tolist()

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get('https://web.whatsapp.com/')
input("Scan the QR code and then press Enter to continue...")

# Locate the group chat
group_name = "Ideathon '24 eCell NSUT"
search_box = driver.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]')
search_box.send_keys(group_name)
time.sleep(2)
search_box.send_keys(Keys.ENTER)

# Wait for the group chat to load
time.sleep(5)

# Add contacts to the group
for phone_number in phone_numbers:
    search_box.send_keys(phone_number)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

# Close the browser window
driver.quit()
