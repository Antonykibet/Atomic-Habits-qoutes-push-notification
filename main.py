import random
import logging
from plyer import notification
from quote import quote

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_quote():
    quotes = quote('Atomic habits')
    if not quotes:
        logging.warning("No quotes found.")
        return
    # Generate a random index to select a quote
    no_of_quotes = len(quotes)
    index = random.randint(0, no_of_quotes-1)
    return quotes[index]['quote']

def send_notification(message, app_name='LOCKDN', title='Atomic Habits'):
    logging.info("Sending notification...")
    notification.notify(
        title=title, message=message, app_name=app_name, timeout=30
    )


if __name__ == "__main__":
    message = get_quote()
    send_notification(message)
    logging.info("Notification sent successfully")