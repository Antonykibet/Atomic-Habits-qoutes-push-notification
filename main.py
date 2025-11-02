import random
from plyer import notification
from quote import quote


def get_quote():
    quotes = quote('Atomic habits')
    # Generate a random index to select a quote
    no_of_quotes = len(quotes)
    index = random.randint(0, no_of_quotes-1)
    return quotes[index]['quote']

def send_notification(message, app_name='LOCKDN', title='Atomic Habits'):
    print("sending notification...")
    notification.notify(
        title=title, message=message, app_name=app_name, timeout=30
    )


if __name__ == "__main__":
    message = get_quote()
    send_notification(message)