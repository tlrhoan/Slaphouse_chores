from collections import deque
import smtplib
from email.message import EmailMessage
from twilio.rest import Client

fname = "/Users/mc98090/desktop/file1.txt"

# opening the file and read contents
my_file = open(fname, "r")
  
# reading the file
data = my_file.read()
data_into_list = data.split("\n")
print("Initial list:")
print(data_into_list)
my_file.close()

# Naming and contact list for housemates
slapHouseResidents= {"Ash": "", "Keyan": "", "Melissa": "", "Brian": "", "Kevin": "", "Tristan":""}
chores = data_into_list
emails={"ash":"7163482003@tmomail.net", "melissa":"3238235882@vtext.com", "tristan":"5597601868@vtext.com", "brian": "9185207346@txt.att.net" , "keyan": "9259899386@vtext.com", "kevin":"8583665910@vtext.com" }
k = 1
j =0
x = deque(chores)
x.rotate(k)
print("Post rotate list:")
print(x) 
chores = list(x)

#Assign all chores
for i in slapHouseResidents:
	slapHouseResidents[i]= x[j]
	j+=1
print("Final chore assignments:")
print(slapHouseResidents)

#Write new list to file
with open(fname, 'w') as f:
    for item in x:
        f.write("%s\n" % item)

# Remove any empty rows
with open(fname) as f_input:
    data = f_input.read().rstrip('\n')

with open(fname, 'w') as f_output:    
    f_output.write(data)


# Sending...

msg = EmailMessage()
msg.set_content('Hi Ash, your chores for the week: ' + slapHouseResidents["Ash"])

msg['Subject'] = 'SLAP HOUSE 4.0 CHORES ALERT'
msg['From'] = "slaphouse4.0@gmail.com"
msg['To'] = emails["ash"]

msg2 = EmailMessage()
msg2.set_content('Hi Melissa, your chore for the week: ' + slapHouseResidents["Melissa"])

msg2['Subject'] = 'SLAP HOUSE 4.0 CHORES ALERT'
msg2['From'] = "slaphouse4.0@gmail.com"
msg2['To'] = emails["melissa"]

msg3 = EmailMessage()
msg3.set_content('Hi Tristan, your chore for the week: ' + slapHouseResidents["Tristan"])

msg3['Subject'] = 'SLAP HOUSE 4.0 CHORES ALERT'
msg3['From'] = "slaphouse4.0@gmail.com"
msg3['To'] = emails["tristan"]

msg4 = EmailMessage()
msg4.set_content('Hi Brian, your chores for the week: ' + slapHouseResidents["Brian"])

msg4['Subject'] = 'SLAP HOUSE 4.0 CHORES ALERT'
msg4['From'] = "slaphouse4.0@gmail.com"
msg4['To'] = emails["brian"]

msg5 = EmailMessage()
msg5.set_content('Hi Keyan, your chores for the week: ' + slapHouseResidents["Keyan"])

msg5['Subject'] = 'SLAP HOUSE 4.0 CHORES ALERT'
msg5['From'] = "slaphouse4.0@gmail.com"
msg5['To'] = emails["keyan"]

msg6 = EmailMessage()
msg6.set_content('Hi Kevin, your chores for the week: ' + slapHouseResidents["Kevin"])

msg6['Subject'] = 'SLAP HOUSE 4.0 CHORES ALERT'
msg6['From'] = "slaphouse4.0@gmail.com"
msg6['To'] = emails["kevin"]


server  = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("slaphouse4.0@gmail.com", "Achintya_716")
server.sendmail("achintya.pillai88@gmail.com", "achintya.pillai88@gmail.com", "Test Slaphouse")
server.send_message(msg)
server.send_message(msg2)
server.send_message(msg3)
server.send_message(msg4)
server.send_message(msg5)
server.send_message(msg6)
server.send_message(msg2)
server.quit()

