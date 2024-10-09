##################### Extra Hard Starting Project ######################


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
from datetime import datetime
import smtplib
import random


""" MY SOLUTION """
# df = pd.read_csv("birthdays.csv")
# data_row = df.iterrows()

# user_info = {
#     "name" : [],
#     "email" : [],
#     "year" :[],
#     "month" : [],
#     "day" : []
# }
# for (index,n) in data_row:
#     user_info["name"].append(n.user)
#     user_info["email"].append(n.email)
#     user_info["year"].append(n.year)
#     user_info["month"].append(n.month)
#     user_info["day"].append(n.day)

# print(user_info)

#
# now = dt.datetime.now()
# month = now.month
# day = now.day
#
# MY_EMAIL = "armstrongspycon27@gmail.com"
# TO = user_info["email"][0]
# MY_PASSWORD = "qxkshkyxzufnioee"

# if user_info["month"][0] == month and user_info["day"][0] == day:
#     with open("letter_templates/letter_1.txt", mode="r") as file:
#         letter_str = file.read().replace("[NAME]", user_info["name"][0])
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#             connection.ehlo()
#             connection.login(MY_EMAIL, MY_PASSWORD)
#             connection.sendmail(from_addr=MY_EMAIL, to_addrs=[TO], msg=f"Subject:Birth Day Wishes\n\n{letter_str}")


""" INSTRUCTOR SOLUTION """

MY_EMAIL = "armstrongspycon27@gmail.com"
""" Insert your own gmail app password"""
MY_PASSWORD = ""

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        # connection.starttls()
        connection.ehlo()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

