#!/usr/bin/env python3
import cgitb
cgitb.enable()
import cgi
import smtplib
import json

print("Content-type: application/json\n")

form = cgi.FieldStorage()
recipient_emails = form.getvalue("emails")
subject = form.getvalue("subject")
body = form.getvalue("body")

# Debugging output
if not recipient_emails or not subject or not body:
    print(json.dumps({
        "status": "error",
        "message": "Missing form data",
        "recipient_emails": recipient_emails,
        "subject": subject,
        "body": body
    }))
    exit()

# Convert comma-separated string of emails to list
email_list = recipient_emails.split(',')

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = "rakakumar5204@gmail.com"
password = "ulap cijl xtny zrsi"  # Ensure you handle passwords securely in real scenarios

# Email content
message = f"Subject: {subject}\n\n{body}"

results = []
# Send email to each recipient
for dest in email_list:
    result = {"email": dest.strip(), "status": "success"}
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, dest.strip(), message)
    except Exception as e:
        result["status"] = "failed"
        result["error"] = str(e)
    results.append(result)

# Output JSON
print(json.dumps(results))
