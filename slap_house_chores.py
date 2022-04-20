from collections import deque
import smtplib
from email.message import EmailMessage
import argparse

def send_chores(filename, remind=False):
    """
    Reads current chore file in directory and rotates chores.
    This will then send the list of chores for all housemates to each housemate via phone smtp.
    """
    # opening the file and read contents
    my_file = open(filename, "r")

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
    if not remind:
        chores.rotate(1)
        print(f"[INFO] Post rotate list: {chores}")
    else:
        print(f"[INFO] Current reminder List (no rotation occurred): {chores}")

    # Assign all chores
    j = 0
    prettyList = simpleList = ""
    for resident in list(slapHouseResidents):
        slapHouseResidents[resident] = chores[j]
        prettyList += f"\n{resident}: {slapHouseResidents[resident]}"
        simpleList += f"{resident}: {slapHouseResidents[resident]}, "
        j += 1
    print(f"[INFO] Final chore assignments:{prettyList}")

    # Write new list to file
    with open(filename, 'w') as f:
        for chore in chores:
            f.write(f'{chore}\n')

    # Login and sending...
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("slaphouse4.0@gmail.com", "Achintya_716")
    #server.sendmail("achintya.pillai88@gmail.com", "achintya.pillai88@gmail.com", "Test Slaphouse")

    for housemate in list(slapHouseResidents):
        msg = EmailMessage()
        content = f'Hi {housemate}, this week\'s chore list:\n{prettyList}'

        # Set email message content and send to housemate
        msg.set_content(content)
        msg['Subject'] = 'SLAP HOUSE 4.0 CHORES ALERT'
        msg['From'] = "slaphouse4.0@gmail.com"
        msg['To'] = emails[housemate]

        server.send_message(msg)

    server.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Housemate Chore Rotator that will senda text to phone via smtp.')
    parser.add_argument("--reminder",
                        action='store_true',
                        help="Add this flag to not rotate chores, just send reminder of chore for the week")

    args = parser.parse_args()

    fname = "choreFile.txt"

    send_chores(fname, args.reminder)
