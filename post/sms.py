from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC3645a4317e861372d52f17f75b2bd4ea'
auth_token = 'c81e95d5af32dd6983b5ab137493b348'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+639676877218'
                 )

print(message.sid)