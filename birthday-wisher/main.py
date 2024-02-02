##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas as pd
import random

today = dt.datetime.now()

# Check for today's birthdays
birthdays = pd.read_csv("random_birthdays.csv")

results = birthdays.loc[birthdays.month == today.month].loc[birthdays.day == today.day]

todays_birthdays = []

if len(results) > 0:
    for (index, row) in results.iterrows():
        todays_birthdays.append({'name': row.first_name, 'email': row.email})

    # Write letters
    letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

    for birthday in todays_birthdays:
        with open(f"letter_templates/{random.choice(letters)}", mode='r') as file:
            letter = file.read()
            birthday['letter'] = letter.replace("[NAME]", birthday['name'])

    # Send emails
    for birthday in todays_birthdays:
        email = birthday['email']
        letter = birthday['letter']

        # Send message to 'email' with body 'letter'

        subject = f"Subject: Happy birthday, dear {birthday['name']}!"
        print(f"{subject}\n\n{email}\n{letter}\n\n")

else:
    print("No birthdays today")