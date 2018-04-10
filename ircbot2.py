import socket
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')

server = "irc.freenode.org"       #settings
channel = "#tesc"
botnick = "Tescbot"
sentUser = False
sentNick = False


irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
print "connecting to:"+server
irc.connect((server, 6667))                                                         #connects to the server
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n") #user authentication
irc.send("NICK "+ botnick +"\n")                            #sets nick
#irc.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth
irc.send("JOIN "+ channel +"\n")
irc.send("Hi I am a bot....killall humanz " + "\n")

def Send(msg):
    irc.send('PRIVMSG ' + channel + ' : ' + msg +  '\r\n')

Send("Whats Up DOC")


try:
	while 1:    #puts it in a loop
		text=irc.recv(2040)
		if len(text) > 0:
			print text
		else:
			continue

		if text.find('!QUACK') != -1:                          #check if 'PING' is found
			Send('A wild duck appears!') #returnes 'PONG' back to the server (prevents pinging out!)
			switch = True
			while switch == True:
				text=irc.recv(2040)
				if len(text) > 0:
					print text
					if text.find("!Bang") != -1:
						Send('DuckShot! You must have quacked my code')
						t = text.split(':!Bang')
						to = t[1].strip()
						Send(str(to)+ " Shot a Duck")
						switch = False
						break
					if text.find("!Befriend") != -1:
						Send('Dawwwww')
						t = text.split(':!Befriend')
						to = t[1].strip()
						Send(str(to)+ "You like Ducks a Ducks!")
						switch = False
						break

except KeyboardInterrupt:
	print "Quit"
	irc.send("Bye\n")
	sys.exit()

