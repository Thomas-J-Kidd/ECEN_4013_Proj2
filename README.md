# ECEN 4013 Fall 2023 Project 2 GPS IMU data sensor

Team members:
- Christopher Hale: Scribe
- Jasmine Taplin: Scrum Master
- Mohammad Alkharaz: Point of Contact
- Thomas Kidd: Repo Oversight

## Budget
- Total Budget: $250
- Current Spending: $58.85
- Amount Left: $191.15


## Due dates
- Sprint 1 progress report - Monday Oct. 30 11:59pm
- Sprint 2 progress report - Monday Nov.13 11:59pm
- Final Demo - Week of Dec. 4th
- Final Report - Friday May 15th 11:59pm (last Friday of finals week)

## Important considerations and TODOs
**Current TODOs**
1) Implement M10 GPS module
    - NMEA GPS communication standard
2) Implement LoRa Module. Details in Software/CircuitPython
3) Implement SD Card Reader. Details in Software/CircuitPython
4) Implement GUI
5) Create specs for PCB, Housing, and power usage

**Past TODOs Done or mitigated**
- <del>Logic Levels (3.3V or 5V) potentially use a level shifter</del>
    - <del> https://learn.sparkfun.com/tutorials/logic-levels/all</del>
- <del>SD card library or reader. SD card communication based on different hex numbers</del>
    - <del>https://docs.micropython.org/en/latest/library/machine.SDCard.html</del>

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

Radio options (from class):
Bluetooth module: HC-05/HC=06
Serial radios: RFM69 (SPI), SX...

PySimpleGUI
    *Needs python and pip
        -pip: https://bootstrap.pypa.io/get-pip.py
        

