from tunes import Tunes
from player import Player
from serial_comm import SerialComm

ser_uart1 = SerialComm()
ser_uart1.start_serial()

print("READY!")

while True:
    if ser_uart1.uart.any():
        print("Incomming data...")
        data = ser_uart1.rcv_data()

        if data.startswith("T"):
        try:
            final_data = eval(data)
            if isinstance(final_data, ):
                print("It is a Tunes instance!")
                Player.play_tune(final_data)
        except NameError:
            print("Not a valid command, ignoring")
