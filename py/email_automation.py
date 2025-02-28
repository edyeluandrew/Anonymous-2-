import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
    # SMTP server details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = "edyelu3@gmail.com"
    password = "zppv hbvx ntdl isxy"

    # Create message
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Send email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, message.as_string())
    server.quit()

# List of recipient emails
recipient_emails = [
    "2023akcs4987gf@kab.ac.ug",
    "edyeluandrew1@gmail.com"
    "edyeluandrew1@gmail.com"
]

# Message details
subject = "Hello from Python"
body = "This is a test email sent from Python. Hope you're doing well!"

# Send email to each recipient
for email in recipient_emails:
    send_email(email, subject, body)
    print(f"Email sent to {email}")
