from twilio.rest import Client 
 
account_sid = 'AC39a4e7af9537c6381d5181d835b5f98b' 
auth_token = '2bbc6b570cbccac29ba22b51ac978368' 
client = Client(account_sid, auth_token) 
 
def send_love():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Wating for your reply',      
                              to='whatsapp:+918368891320' 
                          ) 
 
    print(message.sid)