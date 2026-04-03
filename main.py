from usb_detector import get_usb_devices
from device_auth import is_authorized
from logger import log_event

print("Secure USB Access Control System Started\n")

devices = get_usb_devices()

for device in devices:

    print("Detected Device:", device)

    if is_authorized(device):

        print("ACCESS ALLOWED\n")

        log_event(device + " Allowed")

    else:

        print("ACCESS BLOCKED\n")

        log_event(device + " Blocked")