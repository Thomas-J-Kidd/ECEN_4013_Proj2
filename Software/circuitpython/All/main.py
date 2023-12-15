# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import sdcardio
import storage
import adafruit_gps
import adafruit_rfm9x
from digitalio import DigitalInOut, Direction, Pull

######################################
#            IMU Setup               #
######################################

#from adafruit_lsm6ds.lsm6dsox import LSM6DSOX as LSM6DS

# To use LSM6DS33, comment out the LSM6DSOX import line
# and uncomment the next line
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33 as LSM6DS

# To use ISM330DHCX, comment out the LSM6DSOX import line
# and uncomment the next line
# from adafruit_lsm6ds.lsm330dhcx import ISM330DHCX as LSM6DS

# To use LSM6DS3TR-C, comment out the LSM6DSOX import line
# and uncomment the next line
# from adafruit_lsm6ds.lsm6ds3 import LSM6DS3 as LSM6DS

from adafruit_lis3mdl import LIS3MDL



custom_scl = board.GP1  # Replace with your desired SCL pin.
custom_sda = board.GP0  # Replace with your desired SDA pin.

i2c = busio.I2C(custom_scl, custom_sda) # uses board.SCL and board.SDA

accel_gyro = LSM6DS(i2c)
mag = LIS3MDL(i2c)


######################################
#             GPS Setup              #
######################################

#custom_tx = board.GP4
#custom_rx = board.GP5
#uart = busio.UART(custom_tx, custom_rx, baudrate=9600, timeout=30)
#gps = adafruit_gps.GPS(uart, debug=False)
#last_print = time.monotonic()

######################################
#            LoRa Setup              #
######################################

# costom_spi_sck_right = board.GP10
# custom_spi_mosi_right = board.GP11
# custom_spi_miso_right = board.GP12
# custom_spi_cs_right = board.GP13
# custom_lora_rst_right = board.GP14

# CS_right = DigitalInOut(custom_spi_cs_right)
# RESET_right = DigitalInOut(custom_lora_rst_right)
# spi_right = busio.SPI(costom_spi_sck_right, MOSI=custom_spi_mosi_right, MISO=custom_spi_miso_right)

# try:
#     rfm9x_right = adafruit_rfm9x.RFM9x(spi_right, CS_right, RESET_right, 915.0)
#     print("RFM9X Right Message detected")
#     rfm9x_right.tx_power = 23
#     prev_packet_right = None
# except RuntimeError as error:
#     # Thrown on version mismatch
#     print('RFM9x Right Error: ', error)
    


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

sdcard = sdcardio.SDCard(spi_sd, CS_sd)
vfs = storage.VfsFat(sdcard)

storage.mount(vfs, "/sd")



while True:
    acceleration = accel_gyro.acceleration
    gyro = accel_gyro.gyro
    magnetic = mag.magnetic
    
    ###########################################
    #                   RF
    ###########################################
    # left_module = bytes("Left Module!\r\n","utf-8")
    # rfm9x_left.send(left_module)
    # print("Message sent from left module")
    # 
    # packet_right = None
    
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

    
    
    ###########################################
    #                   GPS
    ###########################################
    #gps.update()

    #current = time.monotonic()
    #if current - last_print >= 1.0:
    #    last_print = current
    #    if not gps.has_fix:
    #        print('Waiting for fix...')
    #        continue
    #    print('=' * 40)  # Print a separator line.
    #    print('Latitude: {0:.6f} degrees'.format(gps.latitude))
    #    print('Longitude: {0:.6f} degrees'.format(gps.longitude))
    #    print('Satellites: ', gps.satellites)
    #    print('Altitude: ', gps.altitude_m)
    #    print('Sats: ', gps.sats)
    
    ###########################################
    #                  IMU
    ###########################################
    #print(
    #    "Acceleration: X:{0:7.2f}, Y:{1:7.2f}, Z:{2:7.2f} m/s^2".format(*acceleration)
    #)
    #print("Gyro          X:{0:7.2f}, Y:{1:7.2f}, Z:{2:7.2f} rad/s".format(*gyro))
    #print("Magnetic      X:{0:7.2f}, Y:{1:7.2f}, Z:{2:7.2f} uT".format(*magnetic))
    #print("")
    #time.sleep(0.5)
    ###########################################
    time.sleep(0.1)

