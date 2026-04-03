from datetime import datetime

def log_event(message):

    with open("logs/usb_log.txt", "a") as file:

        time = datetime.now()

        file.write(f"{time} : {message}\n")