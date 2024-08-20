from display import Display
from player import Player
from serial_comm import SerialComm
from command_processor import CommandProcessor

# Starts Serial
ser_uart1 = SerialComm()
ser_uart1.start_serial()

led_disp = Display()

# Starts Command Processor
com_processor = CommandProcessor(
    {
        "T":Player.eval_and_play,
        "D":led_disp.eval_display,
     }
)

print("READY!")

while True:
    if ser_uart1.incomming_data():
        print("Incomming data...")
        data = ser_uart1.rcv_data()
        print(data)
        com_processor.route(data)

