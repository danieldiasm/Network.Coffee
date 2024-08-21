import serial
import time
from frames import coffee_mug as mug

# Configure the serial connection (COM port, baud rate, etc.)
ser = serial.Serial(
    port='COM5',       # Replace with your port
    baudrate=57600,     # Set the baud rate to match the device
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1          # Set a timeout for reading (optional)
)

def send_data(data):
    if ser.is_open:
        ser.write(data.encode())  # Send the data as bytes
        print(f"Sent: {data}")
    else:
        print("Serial port is not open")

def close_serial():
    if ser.is_open:
        ser.close()
        print("Serial port closed")

# Main loop (or just one-time send)
try:
    while True:
        # data = input("Enter data to send (type 'exit' to quit): ")
        # if data.lower() == 'exit':
        #    break
        # send_data(data+"\n")
        for i in mug:
            send_data(f"D{i}"+"\n")
            time.sleep(1)  # Short delay before the next send (optional)
except KeyboardInterrupt:
    print("\nGraceful stop: KeyboardInterrupt received")
finally:
    close_serial()
    print("Program exited cleanly.")
