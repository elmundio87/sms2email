import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText


phonebook = {'+447732310238': 'Tara Jane Copeman', '+447411739726': 'Edmund Dipple'}


def contactList(number):
        try:
                return phonebook[number]
        except:
		print "Can't find contact"
                return number

msg = 'Location 0, folder "Inbox", SIM memory, Inbox folder\nSMS message\nSMSC number          : "+447782000800"\nSent                 : Sun 19 Feb 2012 13:55:24  +0000\nCoding               : Default GSM alphabet (no compression)\nRemote number        : "+447732310238"\nStatus               : UnRead\n\nPing\n\nlol\n\nLocation 1, folder "Inbox", SIM memory, Inbox folder\nSMS message\nSMSC number          : "+447782000800"\nSent                 : Sun 19 Feb 2012 13:55:24  +0000\nCoding               : Default GSM alphabet (no compression)\nRemote number        : "+447411739726"\nStatus               : UnRead\n\nPing\n\n'

#print msg

list = msg.split("\n")

state = 0
msgCounter = 0
date = ""
sender = "" 
msgText = ""
msg = {"body":""}

for x in range(0,len(list)):	
	#print state
	#print list[x]
	if state == 0:
		#print list[x]
			
		if list[x] == "":
			state = 1
		
		try:
			msg[list[x].split(":")[0].strip()] = list[x].split(":")[1].replace('"',"").strip()
		except:
			continue
		
	
		continue
	if state == 1:
			if list[x] == 'Location ' + str(msgCounter + 1) +  ', folder "Inbox", SIM memory, Inbox folder' or x == len(list) - 1:
				msg['Remote number'] = contactList(msg['Remote number'])
				email = MIMEText(msgText)
				s = smtplib.SMTP('smtp.gmail.com:587')
				s.starttls()
				s.login('elmundio1987@gmail.com','fwlgmgvnxcebqxea')
				email['Subject'] = 'SMS from ' + msg['Remote number']
				email['From'] = msg['Remote number'] 
				email['To'] = 'elmundio1987.sms@gmail.com'
				print "Subject: " + email['Subject']
				print "Sender: " + msg['Remote number']
				print "Body:" + msg['body']
				s.sendmail('elmundio1987.sms@gmail.com', 'elmundio1987.sms@gmail.com', email.as_string())
				s.quit()
				print "Sent email"
				msgCounter += 1
				state = 0
				msg = {"body":""}
			else:
				msg['body'] += list[x] + "\n"
			continue
	
