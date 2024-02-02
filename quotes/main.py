import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

EMAIL = os.environ.get("EMAIL")

def get_quote():
    import random

    with open("quotes.txt", mode="r") as file:
        quotes = file.readlines()

    quote = random.choice(quotes).split("–")

    return { "text":  quote[0], "author":  quote[1].strip() }


def send_emai(to_addr, subject, body):
    import smtplib

    app_password = os.environ.get("APP_PASSWORD")
    service_email = os.environ.get("SERVICE_EMAIL")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=service_email, password=app_password)
        connection.sendmail(
            from_addr=service_email, 
            to_addrs=to_addr, 
            msg=f"Subject:{subject}\n\n{body}"
        )


quote = get_quote()
print(quote)

now = dt.datetime.now()

day_of_week = { 0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday" }

if now.weekday() == 6:
    print(f"Today is {day_of_week[now.weekday()]}")

    to_addr = EMAIL
    subject = "Quote of the Day!"
    body = f"{quote['text']}\n- {quote['author']}"

    print(body)

    send_emai(to_addr, subject, body)