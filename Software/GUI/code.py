
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import time
import board
import busio
import os
import circuitpython_csv as csv
from adafruit_datetime import datetime, date
#import sdcardio
import adafruit_sdcard
import storage
import adafruit_gps
import adafruit_rfm9x
from digitalio import DigitalInOut, Direction, Pull
import microcontroller

######################################
#            IMU Setup               #
######################################
# from adafruit_lsm6ds.lsm6ds33 import LSM6DS33 as LSM6DS
# from adafruit_lis3mdl import LIS3MDL

# custom_scl = board.GP21  # Replace with your desired SCL pin.
# custom_sda = board.GP20  # Replace with your desired SDA pin.

# i2c = busio.I2C(custom_scl, custom_sda) # uses board.SCL and board.SDA

# accel_gyro = LSM6DS(i2c)
# mag = LIS3MDL(i2c)


######################################
#             GPS Setup              #
######################################

# custom_tx = board.GP4
# custom_rx = board.GP5
# uart = busio.UART(custom_tx, custom_rx, baudrate=9600, timeout=30)
# gps = adafruit_gps.GPS(uart, debug=False)
# last_print = time.monotonic()

######################################
#            LoRa Setup              #
######################################

costom_spi_sck_right = board.GP10
custom_spi_mosi_right = board.GP11
custom_spi_miso_right = board.GP12
custom_spi_cs_right = board.GP13
custom_lora_rst_right = board.GP14

CS_right = DigitalInOut(custom_spi_cs_right)
RESET_right = DigitalInOut(custom_lora_rst_right)
spi_right = busio.SPI(costom_spi_sck_right, MOSI=custom_spi_mosi_right, MISO=custom_spi_miso_right)

try:
    rfm9x_right = adafruit_rfm9x.RFM9x(spi_right, CS_right, RESET_right, 915.0)
    print("RFM9X Right Message detected")
    rfm9x_right.tx_power = 23
    prev_packet_right = None
except RuntimeError as error:
    # Thrown on version mismatch
    print('RFM9x Right Error: ', error)
    


# costom_spi_sck_left = board.GP2
# custom_spi_mosi_left = board.GP3
# custom_spi_miso_left = board.GP4
# custom_spi_cs_left = board.GP5
# custom_lora_rst_left = board.GP6

# CS_left = DigitalInOut(custom_spi_cs_left)
# RESET_left = DigitalInOut(custom_lora_rst_left)
# spi_left = busio.SPI(costom_spi_sck_left, MOSI=custom_spi_mosi_left, MISO=custom_spi_miso_left)

# try:
#     rfm9x_left = adafruit_rfm9x.RFM9x(spi_left, CS_left, RESET_left, 915.0)
#     print("RFM9X Left Message detected")
#     rfm9x_left.tx_power = 23
#     prev_packet_left = None
# except RuntimeError as error:
#     print("RFM9X Left Error: ", error)
#     
######################################
#               SD Card Setup        #
######################################

costom_spi_sck_sd = board.GP18
custom_spi_mosi_sd = board.GP19
custom_spi_miso_sd = board.GP16
custom_spi_cs_sd = board.GP17


CS_sd = DigitalInOut(custom_spi_cs_sd)
spi_sd = busio.SPI(costom_spi_sck_sd, MOSI=custom_spi_mosi_sd, MISO=custom_spi_miso_sd)

sdcard = adafruit_sdcard.SDCard(spi_sd, CS_sd)
vfs = storage.VfsFat(sdcard)

file_path = "/sd/IMU_data.csv"
storage.mount(vfs, "/sd")

def create_csv_with_headers():
    with open(file_path, "w") as f:
        writer = csv.writer(f)
        # Write headers
        writer.writerow(["Year", "Month", "Day", "Hour", "Minute", "Second", "Satellites", "Latitude", "Longitude", "Elevation", "X accel", "Y accel", "Z accel", "X mag", "Y mag", "Z mag", "X Gyro", "Y Gyro", "Z Gyro"])
        f.write("\r\n")
        
def write_data_to_csv(data):
    with open(file_path, "a") as f:
        writer = csv.writer(f)
        # Write data
        writer.writerow(data)
        f.write("\r\n")

try:
    # Attempt to check if the file exists
    os.stat(file_path)
    file_exists = True
except OSError as e:
    # Handle the case where the file doesn't exist
    if e.args[0] == 2:  # Error code 2 indicates "No such file/directory"
        file_exists = False
        # Create the file with headers
        create_csv_with_headers()
    else:
        # Handle other OSError cases
        raise e

# # If the file doesn't exist, create it with headers
if not file_exists:
    create_csv_with_headers()



while True:
    
    
    ###########################################
    #                   GPS
    ###########################################
    # gps.update()
    # current = time.monotonic()
    # if current - last_print >= 1.0:
    #    last_print = current
    #    if not gps.has_fix:
    #        #print('Waiting for fix...')
    #        continue
       #print('=' * 40)  # Print a separator line.
       #print('Latitude: {0:.6f} degrees'.format(gps.latitude))
       #print('Longitude: {0:.6f} degrees'.format(gps.longitude))
       #print('Satellites: ', gps.satellites)
       #print('Altitude: ', gps.altitude_m)
    
    ###########################################
    #                  IMU
    ###########################################
    # acceleration = accel_gyro.acceleration
    # gyro = accel_gyro.gyro
    # magnetic = mag.magnetic
    # print(
    #    "Acceleration: X:{0:7.2f}, Y:{1:7.2f}, Z:{2:7.2f} m/s^2".format(*acceleration)
    # )
    # print("Gyro          X:{0:7.2f}, Y:{1:7.2f}, Z:{2:7.2f} rad/s".format(*gyro))
    # print("Magnetic      X:{0:7.2f}, Y:{1:7.2f}, Z:{2:7.2f} uT".format(*magnetic))
    # print("")
    ###########################################
    
    

    ###########################################
    #                  SD
    ###########################################
    # Example data (replace this with your actual data)
    # date_time_str = datetime.now()
    # print(datetime.now())
    # Parse the date and time string into a struct_time object
    # Access individual components of the parsed time
    print(datetime.timetuple())
    year = date_time_str.year
    month = date_time_str.month
    day = date_time_str.day
    hour = date_time_str.hour
    minute = date_time_str.minute
    second = date_time_str.second
    data_to_write = [
    year,
    month,
    day,
    hour,
    minute,
    second,
    gps.satellites,  # Satellites
    gps.latitude,  # Latitude
    gps.longitude,  # Longitude
    gps.altitude_m,  # Elevation
    acceleration[0],  # X accel
    acceleration[1],  # Y accel
    acceleration[2],  # Z accel
    magnetic[0],  # X mag
    magnetic[1],  # Y mag
    magnetic[2],  # Z mag
    gyro[0],  # X Gyro
    gyro[1],  # Y Gyro
    gyro[2]   # Z Gyro
    ]

    # Write data to CSV
    write_data_to_csv(data_to_write)
    
    print(data_to_write)
    
    # Convert each element to a string
    # data_strings = [str(item) for item in data_to_write]

    # Join the strings into a single string with commas
    # data_string = ",".join(data_strings)
    
    ###########################################
    #                   RF
    ###########################################
    
    
    # right_module = bytes(data_string,"utf-8")
    right_module = bytes('test',"utf-8")
    rfm9x_right.send(right_module)
    #print("Message sent from module")

    # packet_right = None
    # 
    # # check for packet rx
    # packet_right = rfm9x_right.receive()
    # if packet_right is None:
    #     print("Packet received: ", packet_right)
    # else:
    #     # Display the packet text and rssi
    #     prev_packet_right = packet_right
    #     packet_text_right = str(prev_packet_right, "utf-8")
    #     print('RX: ')
    #     print(packet_text_right)
    #     time.sleep(1)
    #print("sending over data from USB")
    print("testing board") 
    # print(f"/{data_to_write}")
    time.sleep(0.1)




