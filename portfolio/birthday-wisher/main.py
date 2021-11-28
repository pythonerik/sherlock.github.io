from datetime import datetime
import pandas
import smtplib
import random

MY_EMAIL = "pythonerik@gmail.com"
MY_PASSWORD = "id4ID$098"

today_tuple = (datetime.now().month, datetime.now().day)

df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(df_row.month, df_row.day): df_row for (index, df_row) in df.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}")
