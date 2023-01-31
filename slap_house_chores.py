#!/usr/bin/env python3

from collections import deque
import smtplib
from email.message import EmailMessage
import argparse

import re
import asyncio
import aiosmtplib

HOST = "smtp.gmail.com"


async def send_chores(filename, remind=False):
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
    # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # server.login("slaphouse4.0@gmail.com", "Achintya_716")
    # server.sendmail("achintya.pillai88@gmail.com", "achintya.pillai88@gmail.com", "Test Slaphouse")

    # GMail settings

    for housemate in list(slapHouseResidents):
        msg = EmailMessage()
        msg2 = EmailMessage()

        # Set email message content and send to housemate
        # content = f'Hi {housemate}, your chore for the week: {slapHouseResidents[housemate]}'
        content = f'Hi {housemate}, this is SlapHouse chores signing off forever. Thanks for keeping Slaphouse clean. \n XOXO'
        msg.set_content(content)
        msg['Subject'] = 'SLAP HOUSE CHORES ALERT'
        msg['From'] = "slaphouse4.0@gmail.com"
        msg['To'] = emails[housemate]

        # send
        send_kws = dict(username="slaphouse4.0@gmail.com", password="bmjjxpzkmhnziyht", hostname=HOST, port=587, start_tls=True)
        res = await aiosmtplib.send(msg, **send_kws)  # type: ignore
        msg = "failed" if not re.search(r"\sOK\s", res[1]) else "succeeded"
        print(msg)

            # server.send_message(msg)

        # # Set message content to full chore list for second text message
        # msg2_content = f'**** Chore List **** {prettyList}'
        # msg2.set_content(msg2_content)
        # msg2['From'] = "slaphouse4.0@gmail.com"
        # msg2['To'] = emails[housemate]
        # server.send_message(msg2)

    # server.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Housemate Chore Rotator that will send a text to phone via smtp.')
    parser.add_argument("--reminder",
                        action='store_true',
                        help="Add this flag to not rotate chores, just send reminder of chore for the week")

    args = parser.parse_args()

    fname = "choreFile.txt"

    asyncio.run(send_chores(fname, args.reminder))
