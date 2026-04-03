import usb.core
import usb.backend.libusb1

backend = usb.backend.libusb1.get_backend()

def get_usb_devices():
    devices = []
    found = usb.core.find(find_all=True, backend=backend)

    for dev in found:
        vendor = hex(dev.idVendor)
        product = hex(dev.idProduct)

        device_id = f"{vendor}:{product}"
        devices.append(device_id)

    return devices