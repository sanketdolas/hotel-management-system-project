import pandas as pd
from twilio.rest import Client

# Twilio account credentials
account_sid = 'ACef4e6bc751036f83302d0388db77528e'
auth_token = 'e5d6adc37351ff685c5209b988b44716'
twilio_phone_number = '+12348039040'


def get_contact_numbers_from_excel(file_path, sheet_name, column_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    contact_numbers = df[column_name].astype(str).tolist()
    return contact_numbers


def send_whatsapp_message(message, recipients):
    client = Client(account_sid, auth_token)
    for recipient in recipients:
        whatsapp_recipient = "whatsapp:" + recipient
        client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=whatsapp_recipient
        )


if __name__ == "__main__":
    file_path = './numbers.xlsx'
    sheet_name = 'Sheet1'  # Change this to the name of your sheet if different
# Change this to the column name containing contact numbers
    column_name = 'ContactNumbers'
    message_to_send = "Hello! This is a sample WhatsApp message sent using Twilio."

    contact_numbers = get_contact_numbers_from_excel(
        file_path, sheet_name, column_name)
    send_whatsapp_message(message_to_send, contact_numbers)
