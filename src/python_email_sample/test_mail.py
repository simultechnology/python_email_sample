# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import Message

textfile = 'sample.txt'

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = Message()
    msg.set_payload(fp.read())

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = f'mail title'
    msg['From'] = 'from@example.net'
    msg['To'] = 'to@example.com'

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost', 1025)
    s.set_debuglevel(True)
    s.send_message(msg)
    s.quit()