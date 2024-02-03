import usb

class USB_on_plug:
    def __init__(self):
        self.event = None
    def on_plug(self, dev, event, user_data):
        """event: 1 - plugged,  event: 2 - unplugged"""
        self.event = event
        print(f'\nDev:{dev}, \nevent:{event}, \nuser data:{user_data}')
        return 0

def on_plug(dev, event, user_data):
    """event: 1 - plugged,  event: 2 - unplugged"""
    print(f'\nDev:{dev}, \nevent:{event}, \nuser data:{user_data}')
    return 0


if __name__ == "__main__":
    # dev = usb.core.find(idVendor=0x090c, idProduct=0x1000)
    # if dev is None:
    #     raise ValueError('Device not found')
    # print(str(hex(dev.idVendor)))
    # print(str(hex(dev.idProduct)))
    usb_plug = USB_on_plug()
    handle = usb.register_callback(usb_plug.on_plug)

    for i, event in enumerate(usb.hotplug.loop()):
        print(usb_plug.event)
        print(f'{i}->{event}{type(event)}')
        if usb_plug.event == 2:
            break

    handle.finalize()