# send motivational quote via email on Monday

import datetime as dt
import smtplib as s
import pandas as p
from random import choice

EMAIL = "example@gmail.com"
PASSWORD = "abcd1234()"
SMTP_SERVER = "smtp.gmail.com"

current_day = dt.datetime.today().weekday()

if current_day == 0:
    with open("quotes.txt") as q_file:
        quotes = q_file.readlines()
        quote_of_day = choice(quotes)
    with s.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="anotheremail@yahoo.com",
            msg=f"Subject: Monday Motivation\n\n{quote_of_day}"
        )
    
else:
    print("It's Not Monday")

