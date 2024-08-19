from tunes import Tunes
from player import Player
from serial_comm import SerialComm

ser_uart1 = SerialComm()
ser_uart1.start_serial()

Player.play_tune(Tunes.beep_beep_tune)
print("READY!")

while True:
    data = ser_uart1.rcv_data()
    if data:
        print("Received data:", data)

