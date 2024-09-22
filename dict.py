
import time
import random
import json
from turtle import title
from email import message
from socket import timeout
from plyer import notification



data = json.load(open('GRE_Words.json'))


def dictionary():
    while True:
        i = random.choice(list((data.keys())))
        print(i)
        word = data[i]
        notification.notify(
            title = i,
            message = word,
            app_icon = r"C:\Users\DELL\Desktop\Dictionary_Notification\icon.ico",
            timeout = 10
        )
        time.sleep(60*30)

dictionary()