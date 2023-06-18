from django.core.mail import EmailMessage
import concurrent.futures


def send_email(subject, message, recipient_list):
    email = EmailMessage(subject, message, to=recipient_list)
    email.send()


def send_email_async(subject, message, recipient_list):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(send_email, subject, message, recipient_list)
        # Wait for the task to complete (optional)
        future.result()
