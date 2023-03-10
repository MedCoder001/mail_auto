import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Set up SMTP server details
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email_address@gmail.com'
smtp_password = 'your_email_password'

# Set up email message
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['Subject'] = 'Email subject line'

# Add message body
body = 'Email message body'
msg.attach(MIMEText(body))

# Add PDF attachment
pdf_file_path = 'path_to_your_pdf_file.pdf'
with open(pdf_file_path, 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='pdf')
    attachment.add_header('Content-Disposition', 'attachment', filename='pdf_file_name.pdf')
    msg.attach(attachment)

# Set up list of recipient email addresses
to_email_list = ['recipient1@example.com', 'recipient2@example.com', 'recipient3@example.com', 'recipient4@example.com', 'recipient5@example.com', 'recipient6@example.com', 'recipient7@example.com', 'recipient8@example.com', 'recipient9@example.com', 'recipient10@example.com']

# Send email to each recipient
for recipient_email in to_email_list:
    msg['To'] = recipient_email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, recipient_email, msg.as_string())
    print(f"Email sent to {recipient_email}")

print("All emails sent!")
