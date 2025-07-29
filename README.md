from twilio.rest import Client

# Replace these with your actual Twilio credentials
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
twilio_number = '+1234567890'  # Your Twilio phone number
destination_number = '+201234567890'  # Number you want to send SMS to

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Twilio! This is a real project.",
    from_=twilio_number,
    to=destination_number
)

print(f"Message sent. SID: {message.sid}")
