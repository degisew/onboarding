from django.core.mail import send_mail, BadHeaderError


def send_email(email, name, due_date, activity_type):
    message = f"""

        Dear {name},

        We have accepted your request to SWIFT service and we are writing this email to inform you that we want to have a {activity_type} on {due_date}. 
        If you have any suggestion or something to tell us, don't hesitate to reach out.

        Sincerely,
        The Haron computers Team
    """
    try:
        send_mail('Security Alert', message, 'jegisew21@gmial.com', [email, 'degisew.mengist21@gmail.com'])
    except BadHeaderError:
        print("Bad Header Error!")