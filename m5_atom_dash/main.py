from display import Display
from player import Player
from serial_comm import SerialComm
from command_processor import CommandProcessor
from push_button import Button

# Starts Serial
ser_uart1 = SerialComm()
ser_uart1.start_serial()
# Setup Display
led_disp = Display()

# Function that sends data for the button press
def send_button_press(arg):
    ser_uart1.send_data(b'01BP')

# Setup Button
button_A = Button("button_a", send_button_press)
button_A.setup_button()

# Starts Command Processor
com_processor = CommandProcessor(
    {
        "T":Player.eval_and_play,
        "D":led_disp.eval_display,
     }
)

print("READY!")

try:
    while True:
        if ser_uart1.incomming_data():
            data = ser_uart1.rcv_data()
            res = com_processor.route(data)
            if res is not None:
                ser_uart1.send_data(res.encode())
except KeyboardInterrupt:
    pass
