from twilio.rest import Client

# Live Twilio credentials
account_sid = 'ACc90bca221b02cce97993cf6a84b6092f'
auth_token = '3393e2e9aec588ab8271d05e10b6b100'
twilio_number = '+18883087202'

# Destination number
destination_number = '+201234567890'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="This is part of my real Twilio project for sending SMS.",
    from_=twilio_number,
    to=destination_number
)

print("Message sent! SID:", message.sid)
