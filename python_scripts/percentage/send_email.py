from email.message import EmailMessage
import smtplib
import ssl

def send_email(subject, body, email_sender, email_password, email_receiver):
    # Create an EmailMessage object
    email_message = EmailMessage()
    email_message["From"] = email_sender
    email_message["To"] = email_receiver
    email_message["Subject"] = subject
    email_message.set_content(body)

    # Try to send the email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp:
            smtp.login(email_sender, email_password)
            smtp.send_message(email_message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

# # Example usage
# subject = "Subject Have a nice day"
# body = "email test "
# email_sender = "gavriel@amiteam.net"
# email_password = "akmz mzqy okrc farh" # A token password ,Not you email password . 
# email_receiver = "yakov@amiteam.net"

# send_email(subject, body, email_sender, email_password, email_receiver)
