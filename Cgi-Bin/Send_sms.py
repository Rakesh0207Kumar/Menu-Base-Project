#!/usr/bin/env python3

import cgi
import cgitb
from twilio.rest import Client

# Enable debugging
cgitb.enable()

# Twilio credentials
account_sid = ''
auth_token = ''

# Function to send SMS
def send_sms():
    form = cgi.FieldStorage()
    to_number = form.getvalue('to')
    message_body = form.getvalue('body')

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        to=to_number,  # Receiver mobile number
        from_='+13254138596'  # Provided by Twilio API
    )
    return message.sid

print("Content-Type: text/html")
print()
print(send_sms())
