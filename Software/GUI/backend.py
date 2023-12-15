import serial
import datetime
def read_uart(port, baudrate=115200):
    labels = [
        "Date",
        "Timestamp",
        "Satellites",
        "Latitude",
        "Longitude",
        "Elevation",
        "X Acceleration",
        "Y Acceleration",
        "Z Acceleration",
        "X Magnetic",
        "Y Magnetic",
        "Z Magnetic",
        "X Gyro",
        "Y Gyro",
        "Z Gyro"
    ]
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Reading UART data from {port}...")
        
        while True:
            # data = ser.readline().decode('utf-8').strip()
            data = ser.readline()
            print(data)
            # if data:
            #     if data[0] == "/":
            #         data = data[1:]
            #         data_list = data.split(',')
            #         data_dict = dict(zip(labels, data_list))
            #         print(f"Received:\n {data_dict}")

    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace '/dev/ttyUSB0' with the actual serial port of your Raspberry Pi Pico
    serial_port = '/dev/ttyACM0'

    
    # You can adjust the baudrate based on your Pico's configuration
    baud_rate = 115200
    
    read_uart(serial_port, baud_rate)
