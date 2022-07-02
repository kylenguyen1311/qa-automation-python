from distutils.log import info


class Watch:
    serial = None
    firmware = None

    def __init__(self, serial, firmware) -> None:
        self.serial = serial
        self.firmware = firmware

    def info(self):
        print(self.firmware)
        print(self.serial)

    def pair(self):
        pass


watch1 = Watch ("K6F012345666","FSL.1012212.1122")
watch1.info()
