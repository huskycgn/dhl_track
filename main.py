import trackerclass
import telebot
from cred import *
from time import sleep
from datetime import datetime

# List of tracking numbers - just paste yours.
tr_numberlist = TRACKING_NUMBER

tr = trackerclass.Tracker()


def send_message(message):
    bot = telebot.TeleBot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)


curr_str = []

for n in tr_numberlist:
    curr_str.append((n, tr.getstatus(n)['status']))

# print(curr_str)

while True:
    try:
        for i, n in enumerate(tr_numberlist):
            # print(curr_str[i])
            new_str = n, tr.getstatus(n)['status']
            print(datetime.now())
            print(new_str)
            if curr_str[i] != new_str:
                curr_str[i] = new_str
                msg_string = str(f'{new_str[0][0]}:\n{new_str[0][1]}')
                send_message(msg_string)
    except ConnectionError:
        continue
    sleep(360)