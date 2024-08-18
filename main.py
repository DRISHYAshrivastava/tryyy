from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Specify the path to chromedriver
chrome_service = Service('/path/to/chromedriver')
options = webdriver.ChromeOptions()

# Enable headless mode if necessary
# options.add_argument('--headless')

# Setup the Chrome WebDriver
driver = webdriver.Chrome(service=chrome_service, options=options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for user to scan the QR code
print("Scan the QR code and press Enter")
input()

# List of contacts to send messages to
contacts = ['Contact Name 1', 'Contact Name 2']
message = "Your message here"

for contact in contacts:
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(contact)
    time.sleep(2)

    contact_element = driver.find_element(By.XPATH, f'//span[@title="{contact}"]')
    contact_element.click()

    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    message_box.send_keys(message)
    message_box.send_keys('\n')

    time.sleep(1)

driver.quit()
