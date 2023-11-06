import time
import board
import busio
import adafruit_gps

custom_tx = board.GP4
custom_rx = board.GP5

uart = busio.UART(custom_tx, custom_rx, baudrate=9600, timeout=30)

gps = adafruit_gps.GPS(uart, debug=False)
last_print = time.monotonic()

while True:
    acceleration = accel_gyro.acceleration
    gyro = accel_gyro.gyro
    magnetic = mag.magnetic
    gps.update()

    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            print('Waiting for fix...')
            continue
        print('=' * 40)  # Print a separator line.
        print('Latitude: {0:.6f} degrees'.format(gps.latitude))
        print('Longitude: {0:.6f} degrees'.format(gps.longitude))
        print('Satellites: ', gps.satellites)
    
