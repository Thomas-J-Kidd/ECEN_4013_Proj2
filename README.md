# ECEN 4013 Fall 2023 Project 2 GPS IMU data sensor

Team members:
- Christopher Hale
- Jasmine Taplin
- Mohammad Alkharaz
- Thomas Kidd

## Due dates
- Sprint 1 progress report - Monday Oct. 30 11:59pm
- Sprint 2 progress report - Monday Nov.13 11:59pm
- Final Demo - Week of Dec. 4th
- Final Report - Friday May 15th 11:59pm (last Friday of finals week)

## Project Description

1) Create a localization device that will gather GPS data (lat, long, elevation, satellites)
2) Capture IMU data (angular velocity, acceleration, magnetic field -> all in X,Y,Z)
3) Create a CSV data file that is stored on: (ALL OUTPUTS MUST BE AVAILABLE AT THE SAME TIME)
    * SD card continously (use a library)
    * USB port for data stream
    * radio transmitter data stream (some chips have built in BLT, LoRa?)
4) Create a GUI interface that will run on a OS of our choosing
    * Start Display button that will display data from USB
        - Display both GPS and IMU real time update
    * The GUI should not scroll data
    * End display button
    * a way to exit the app
5) Include a display that tells us when we locked on to satellites
6) battery powered (portable)
7) Run for at least one hour
8) a fitted case
9) fabricated circuit board

## Fair game

All modern processors are fair game. Your GPS, IMU, and radio modules must be
separate from your processing device. I do not want a COTS all-in-one solution. You
have a budget of $250 for parts that cannot be found in the part store. The team that
produces a working design of the smallest form factor (case included) will be awarded a
grade ‘bonus’ of 5 points on the project report grade.

## Important considerations and TODOs
1) Logic Levels (3.3V or 5V) potentially use a level shifter
    - https://learn.sparkfun.com/tutorials/logic-levels/all
2) SD card library or reader. SD card communication based on different hex numbers
    - https://docs.micropython.org/en/latest/library/machine.SDCard.html
3) GPS information modeling 
    - U-blox GNSS modules: https://www.u-blox.com/en/product/neo-f10n-module
    - NMEA GPS communication standard
4) IMU 
    - https://cdn.sparkfun.com/assets/7/f/e/c/d/DS-000189-ICM-20948-v1.3.pdf
