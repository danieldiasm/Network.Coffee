# Serial Communication Module

class SerialComm:

    def __init__(self, tx, rx, baud_rate) -> None:
        self.tx = tx
        self.rx = rx
        self.baud_rate = baud_rate

    def rcv_data(self):
        pass

    def send_data(self):
        pass
