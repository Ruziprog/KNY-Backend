from celery import shared_task

@shared_task
def send_welcome_email(user_email):
    print(f"Письмо отправлено {user_email}")
    return f"Done: {user_email}"
