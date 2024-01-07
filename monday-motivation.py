import smtplib
from random import choice
import datetime as dt

my_email = "XXXXXXXXXXXXXXXXX"
password = "XXXXXXXXXXXXXXXXX"

send_count = 0

while True:
    now = dt.datetime.now()
    if now.weekday() == 4:
        send_count += 1
        if send_count < 2:
            with open("quotes.txt", "r") as quotes:
                quotes_list = quotes.readlines()
            random_quote = choice(quotes_list)

            bold_quote = f"<b style='font-size:15px'>{random_quote.strip()}</b>"
            message = f"Subject:Monday Motivation\n"
            message += f"MIME-Version: 1.0\n"
            message += f"Content-Type: text/html\n\n"
            message += bold_quote

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="alex.yermakov20@gmail.com", msg=message)
    else:
        send_count = 0
