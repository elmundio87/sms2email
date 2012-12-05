import commands
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

phonebook = {'+447732310238': 'Tara Jane Copeman', '+447411739726': 'Edmund Dipple'}
state = 0
msgCounter = 0
date = ""
sender = "" 
msgText = ""
msg = {"body":""}



def contactList(number):
        try:
                return phonebook[number]
        except:
		print "Can't find contact"
                return number

sms = commands.getoutput("gammu --geteachsms")

if str.find(sms, "0 SMS parts") != -1:
	print "No SMS messages found, aborting"
	exit()

if str.find(sms, "No response in specified timeout. Probably phone not connected.") != -1:
	exit()

# Create a text/plain message
print sms
list = sms.split("\n")


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
				email = MIMEText(msg['body'])
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




commands.getoutput("gammu --deleteallsms 1")
