def is_authorized(device_id):

    try:

        with open("database/authorized_devices.txt", "r") as file:

            devices = file.read().splitlines()

            if device_id in devices:
                return True
            else:
                return False

    except:

        print("Authorized device list not found")
        return False