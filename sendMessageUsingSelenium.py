import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pywhatkit as kit


def send_whatsapp_message(message, recipients):
    # Launch the web browser and open WhatsApp Web
    driver = webdriver.Chrome()  # Replace with appropriate web driver (e.g., Firefox)
    driver.get("https://web.whatsapp.com")

    # Wait for the user to scan the QR code to log in
    input("Please scan the QR code and press Enter after login...")

    # Loop through recipients and send messages
    # for recipient in recipients:
    #     try:
    #         # Open a chat with the recipient
    #         search_box = WebDriverWait(driver, 2).until(
    #             EC.element_to_be_clickable(
    #                 (By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    #         )
    #         search_box.send_keys(recipient)
    #         time.sleep(2)  # Wait for search results to load
    #         search_box.send_keys(Keys.ENTER)
    #         time.sleep(2)  # Wait for the chat to open

    #         # Type and send the message
    #         message_box = WebDriverWait(driver, 2).until(
    #             EC.element_to_be_clickable(
    #                 (By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]'))
    #         )
    #         message_box.send_keys(message)
    #         # To add a new line if needed
    #         message_box.send_keys(Keys.SHIFT + Keys.ENTER)
    #         message_box.send_keys(Keys.ENTER)

    #         time.sleep(2)  # Wait before sending the next message
    #     except Exception as e:
    #         print(f"Failed to send message to {recipient}. Error: {e}")

    # # Close the web browser after sending all messages
    # driver.quit()


# def send_whatsapp_message(message, recipients):
#     for recipient in recipients:
#         try:
#             kit.sendwhatmsg_instantly(recipient, message, wait_time=10)
#             print(f"Message sent to {recipient} successfully.")
#         except Exception as e:
#             print(f"Failed to send message to {recipient}. Error: {e}")


if __name__ == "__main__":
    file_path = './numbers.xlsx'
    sheet_name = 'Sheet1'  # Change this to the name of your sheet if different
    # Change this to the column name containing contact numbers
    column_name = 'ContactNumbers'
    message_to_send = "Hello! This is a sample WhatsApp message sent using Selenium and WhatsApp Web."

    # Read contact numbers from the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    contact_numbers = df[column_name].astype(str).tolist()

    send_whatsapp_message(message_to_send, contact_numbers)
