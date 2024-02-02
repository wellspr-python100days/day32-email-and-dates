import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

app_password = os.environ.get("APP_PASSWORD")
service_email = os.environ.get("SERVICE_EMAIL")
email = os.environ.get("EMAIL")

subject = "Testing once more"
body = "Hello there again!"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=service_email, password=app_password)
    connection.sendmail(
        from_addr=service_email, 
        to_addrs=email, 
        msg=f"Subject:{subject}\n\n{body}"    
    )
