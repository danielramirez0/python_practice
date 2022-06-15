import datetime as dt
import pandas
from random import choice
from credentials import cred
from libs.email_client import send_email

DATA = pandas.read_csv("birthdays.csv")
RECORDS = DATA.to_dict(orient="records")
# RECORDS = {(row.month, row.day): row for (index, row) in DATA.iterrows()} # Angela's solution
TEMPLATE_FILES = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
TIME = dt.datetime.now()

todays_date = f"{TIME.month:02d}-{TIME.day:02d}"

for record in RECORDS:
    birthday = f'{record["month"]:02d}-{record["day"]:02d}'
    if todays_date == birthday:
        with open(f"letter_templates/{choice(TEMPLATE_FILES)}") as template:
            # card = "".join(line.replace("[NAME]", record["name"]) for line in template.readlines())
            card = template.read().replace("[NAME]", record["name"])
        send_email(record["email"], cred, "Happy Birthday", card)