import serial
import threading
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

running = True

def send_data():
    global running
    while running:
        for i in mug:
            if ser.is_open:
                data = f"D{i}"+"\n"
                ser.write(data.encode("utf-8"))  # Send the data as bytes
                print(f"Sent data")
                time.sleep(0.5)
            else:
                print("Serial port is not open")
                running = False

def receive_data():
    global running
    while running:
        if ser.in_waiting > 0:
            # Read
            incoming_data = ser.readline().decode().strip()
            if incoming_data:
                print(f"Received: {incoming_data}")

def close_serial():
    if ser.is_open:
        ser.close()
        print("Serial port closed")

# Setup and Start sending and receiving threads
send_thread = threading.Thread(target=send_data)
receive_thread = threading.Thread(target=receive_data)

send_thread.start()
receive_thread.start()

def graceful_stop():
    global running
    running = False
    # give time of the threads to end
    time.sleep(1)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nKeyboardInterrupt received!")
    graceful_stop()
finally:
    send_thread.join()
    receive_thread.join()
    close_serial()
    print("Program exited cleanly.")
