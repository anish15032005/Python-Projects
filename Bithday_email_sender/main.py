import smtplib
import datetime as dt 
import random
import pandas as pd  
from email.mime.text import MIMEText
from email.header import Header

# Load the birthdays data from the CSV file
birthdays_data = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
# print(now)
year = now.year
month = now.month
time = now.time()
day_of_week = now.weekday()  # Monday is 0, Sunday is 6
my_email = "mikewazoski1991@gmail.com"

def send_email(person_name, person_email):
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    connection.login(user=my_email, password="your_password")  # Replace with your actual password

    # Read a quote from a file and send it in the email
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)  # Get the random quote
        # print(quote.strip())  # Print the quote without extra newline characters

    body = (
        f"Happy Birthday {person_name}, \n\n"
        f"Wishing you a very Happy Birthday! 🎂\n"
        "May this year bring you loads of happiness, good health, and success in everything you do.\n\n"
        "Enjoy your special day to the fullest — you deserve it!\n\n"
        "Warm wishes,\nAnish"
    )

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = Header("Happy Birthday!", "utf-8")
    msg["From"] = my_email
    msg["To"] = person_email
    msg["Reply-To"] = my_email

    connection.sendmail(
        from_addr=my_email,
        to_addrs=person_email,
        msg=msg.as_string()
    )
    connection.close()  # Close the connection
    
# Check if today is Birthday of anyone
for index, row in birthdays_data.iterrows():
    # Check if the month and day match today's date
    if row['month'] == month and row['day'] == now.day:
        # If it matches, send an email
        person_name = row['name']
        person_email = row['email']
        print(f"Sending birthday wishes to {person_name} at {person_email}")
        send_email(person_name, person_email)












