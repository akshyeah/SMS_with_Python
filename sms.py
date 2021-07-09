from twilio.rest import Client 
 
account_sid = 'AC24d5683df5a21610b3a2121474e3b03e' 
auth_token = '[Auth Token]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGc46faecba598a1dcc7ab7a0b206ee79b', 
                              body='Hey! My chubby, If I could order your steps, I’ll have brought you my way quite sooner than now. 😘 ❤',      
                              to='+919773502080' 
                          ) 
 
print(message.sid)
print('Message sent successfully!')
