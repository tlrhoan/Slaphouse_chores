from collections import deque
import smtplib
from email.message import EmailMessage

fname = "choreFile.txt"

# opening the file and read contents
my_file = open(fname, "r")

# reading the file and removing any empty strings
data = my_file.read()
data_into_list = data.split("\n")
data_into_list = ' '.join(data_into_list).split()
print(f'[INFO] Initial list: {data_into_list}')
my_file.close()

# Naming and contact list for housemates
slapHouseResidents = {"Ash": "",
                      "Keyan": "",
                      "Melissa": "",
                      "Brian": "",
                      "Kevin": "",
                      "Tristan": ""
                      }
emails = {"Ash": "7163482003@tmomail.net",
          "Melissa": "3238235882@vtext.com",
          "Tristan": "5597601868@vtext.com",
          "Brian": "9185207346@txt.att.net",
          "Keyan": "9259899386@vtext.com",
          "Kevin": "8583665910@vtext.com"
          }

chores = deque(data_into_list)
chores.rotate(1)
print(f"[INFO] Post rotate list: {chores}")

# Assign all chores
j = 0
prettyList = simpleList = ""
for resident in list(slapHouseResidents):
    slapHouseResidents[resident] = chores[j]
    prettyList += f"\n{resident}: {slapHouseResidents[resident]}"
    simpleList += f"{resident}: {slapHouseResidents[resident]} "
    j += 1
print(f"[INFO] Final chore assignments:{prettyList}")

# Write new list to file
with open(fname, 'w') as f:
    for chore in chores:
        f.write(f'{chore}\n')

# Login and sending...
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("slaphouse4.0@gmail.com", "Achintya_716")
#server.sendmail("achintya.pillai88@gmail.com", "achintya.pillai88@gmail.com", "Test Slaphouse")

for housemate in list(slapHouseResidents):
    if housemate == "Tristan":
        msg = EmailMessage()
        content = f'Hi {housemate}, this week\'s chore list:{prettyList}\n'

        # Set email message content and send to housemate
        msg.set_content(content)
        msg['Subject'] = 'SLAP HOUSE 4.0 CHORES ALERT'
        msg['From'] = "slaphouse4.0@gmail.com"
        msg['To'] = emails[housemate]

        server.send_message(msg)

server.quit()
