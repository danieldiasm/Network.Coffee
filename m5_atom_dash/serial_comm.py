# Serial Communication Module
from machine import UART


class SerialComm:

    def __init__(self, tx=22, rx=19, baud_rate=57600) -> None:
        self.tx = tx
        self.rx = rx
        self.baud_rate = baud_rate
        self.uart_id = 1
        self.uart = UART(self.uart_id, 
                         self.baud_rate,
                         tx=self.tx,
                         rx=self.rx)

    def start_serial(self):
        '''
        Starts the serial communication opening serial port.
        '''
        self.uart.init()
    

    def close_serial(self):
        '''
        Closes serial connection and returns a new instance of the SerialComm.
        Its renewed since when a connection is closed it cannot be reopened.
        '''
        self.uart.deinit()
        return SerialComm()


    def rcv_data(self):
        '''
        Receives data from the defined port until it gets a line break.
        '''
        buffer = ''
        try:
            while True:
                byte = self.uart.read(1)
                if byte is not None:
                    buffer += byte.decode()
                if byte == b"\n":
                    break
            return buffer
        except UnicodeError as e:
            return f"Unicode Error: Invalid Character"
    

    def send_data(self, data):
        '''
        Send data over the already opened serial connection.
        '''
        self.uart.write(data)

    def incomming_data(self):
        ''' Returns the same as uart.any(), just a wrapper for simplification'''
        return self.uart.any()