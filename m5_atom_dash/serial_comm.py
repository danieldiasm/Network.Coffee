# Serial Communication Module
from machine import UART

class SerialComm:

    def __init__(self, tx=22, rx=19, baud_rate=9600) -> None:
        self.tx = tx
        self.rx = rx
        self.baud_rate = baud_rate
        self.uart_id = 1
        self.uart = UART(self.uart_id, 
                         self.baud_rate,
                         tx=self.tx,
                         rx=self.rx)

    def start_serial(self):
        self.uart.init()

    def rcv_data(self):
        buffer = ''
        while True:
            print(self.uart.any())
            byte = self.uart.read(1)
            if byte is not None:
                print(byte.decode('utf-8'))
                buffer += byte.decode()
            if byte == b"\n":
                break
        return buffer
    
    def send_data(self, data):
        self.uart.write(data)

    def decode_data(self):
        pass
