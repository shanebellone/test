import serial
class GsmModem:
    baud_rate = 115200
    device = "/dev/ttyUSB2"
    modem = serial.Serial(device, baud_rate)

    def __init__(self, command=None, payload=None):
        if command is not None:
            command = str(command).lower()
            at_command = self.prepare_at_command(command, payload)
            last_command, response = self.write(at_command)
            print(last_command, response)


    def write(self, at_command):
        self.modem.write(bytes(at_command + "\r"))
        last_command, response = self.modem.readline(), self.modem.readline()
        return last_command, response

    @staticmethod
    def execute_at_command(self, at_command):
        self.write(at_command)

    @staticmethod
    def prepare_at_command(command, payload):
        # Placeholder for payload
        payload_tag = "{payload_tag}"
        match command:
            case "get status":
                translated_command = 'AT'
            case "send sms":
                translated_command = 'AT+CMGS="+{payload_tag}"'.replace(payload_tag, payload)
            case other:
                return KeyError
        return translated_command


if __name__ == "__main__":
    # payload = "19593338363"
    # GsmModem("send sms", payload=payload)
    GsmModem("get status")

