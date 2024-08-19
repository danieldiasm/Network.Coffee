# Serial Communication Module
from machine import UART

class SerialComm:

    def __init__(self, tx=22, rx=19, baud_rate=9600, timeout=1000) -> None:
        self.tx = tx
        self.rx = rx
        self.baud_rate = baud_rate
        self.uart_id = 1
        self.timeout = timeout
        self.uart = UART(self.uart_id, 
                         self.baud_rate,
                         tx=self.tx,
                         rx=self.rx)

    def start_serial(self):
        self.uart.init()

    def rcv_data(self):
        if self.uart.any():
            data = self.uart.read()
            if data:
                return data.decode('utf-8')
        return None
    
    def send_data(self, data):
        self.uart.write(data)

    def decode_data(self):
        pass
