from twilio.rest import Client
from credentials import account_sid , auth_token, my_cell, my_twilio

client = Client(account_sid , auth_token)

x = ['Rushi \n' for i in range(10)]
my_msg = ''.join(x)



message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)