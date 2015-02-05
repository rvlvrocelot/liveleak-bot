import xmpp

liveleakmessage = "Hello, this is Andrew Bot, I noticed that you have sent me a liveleak link. I just wanted to let you know that there is a 5% chance I will view this link"

def messageCB(sess,mess):
    nick=mess.getFrom().getResource()
    text=mess.getBody()
    fromUser = mess.getFrom()
    
    if text is not None:
        if "liveleak.com" in text:
            
            client = xmpp.Client('facebook.com',debug=[])
            client.connect(server=('chat.facebook.com',5222))
            client.auth(username, passwd)
            client.sendInitPresence()
            message = xmpp.Message(fromUser, liveleakmessage)
            message.setAttr('type', 'chat')
            client.send(message)
        
        else:
            print "no liveleak"

username = '##########PUT USERNAME HERE$############'
passwd = '##########PUT PASSWORD HERE$############'

client = xmpp.Client('facebook.com',debug=[])
client.connect(server=('chat.facebook.com',5222))
client.auth(username, passwd)
client.sendInitPresence()
client.RegisterHandler('message',messageCB)

while 1:
    client.Process(1)
