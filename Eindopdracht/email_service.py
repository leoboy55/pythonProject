# imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# variables
sender_email = "testapihva@gmail.com"
sender_pas = "rucx hgzx mvsw lelf"
receiver_email = "thomasleonardojr@gmail.com"
mail_subject = "Ethereum has reached target."
mail_content_target = "Ethereum has reached the target:"
mail_content_value = "Ethereum is currently worth:"
mail_content_history = "Ethereum prices in the past:"

gmail_address = "smtp.gmail.com"
port_number = 587
successfully_msg = "successfully mail sent"


# goal: Start the email proces
# parameters: (string) ethereum prices, (double) amount notification, current
def prepare_mail(ethereum_prices_string, notification_amount, ethereum_price):
    # mail setup
    message = setup_mine()
    # mail body setup
    setup_body(message, ethereum_prices_string, notification_amount, ethereum_price)
    # sending the mail
    send_smtp_mail(message)


# responsible for creating a mine
def setup_mine():
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = mail_subject
    return message


# responsible for creating mail body
def setup_body(message, ethereum_prices_string, notification_amount, ethereum_price):
    # format float to 2 decimal
    notification_amount = f"{notification_amount:.2f}"
    # make message content with current Ethereum price and target price
    mail_content_final = (f"{mail_content_target} {notification_amount} EUR"
                          f"\n{mail_content_value} {ethereum_price} EUR"
                          f"\n{mail_content_history} {ethereum_prices_string}")
    # attach the content to the message
    message.attach(MIMEText(mail_content_final, 'plain'))


# responsible for sending the mail
def send_smtp_mail(message):
    # create_smtp_session
    session = smtplib.SMTP(gmail_address, port_number)
    # enable tls security
    session.starttls()
    # login to mail
    session.login(sender_email, sender_pas)
    # retrieve message
    text = message.as_string()
    # send mail
    session.sendmail(sender_email, receiver_email, text)
    # log out
    session.quit()
    print(successfully_msg)
