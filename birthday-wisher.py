import smtplib
import time

import pandas as pd
from random import choice
import datetime as dt

my_email = "its.already.2024@gmail.com"
password = "bywz ajkg nrpu dmkl"


birthdays = pd.read_csv("birthdays.csv")
birthdays = pd.DataFrame(birthdays)

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
months = [i for i in birthdays.month]
days = [i for i in birthdays.day]

send_cnt = 0

while True:
    now = dt.datetime.now()
    if now.month in months and now.day in days and now.hour == 21:
        send_cnt += 1
        if send_cnt < 2:
            letter = choice(letters)
            with open(f'letter_templates/{letter}', "r") as file:
                text = file.read()
                name = birthdays[(birthdays['month'] == now.month) & (birthdays['day'] == now.day)].name.item()
            text = text.replace("[NAME]", name)
            text = f'Subject: Happy Birthday, {name}!!!\n\n{text}'
            email = birthdays[birthdays['name'] == name].email.item()
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=email, msg=text)
                time.sleep(3600) 
    else:
        send_cnt = 0
