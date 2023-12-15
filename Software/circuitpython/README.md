# CircuitPython

Circuit python is written by adafruit. They are based on micropython, but added some libraries to make it easier to use some of their breakout boards. The devices are easy to use. 

## Initial Setp

CircuitPython needs to be flashed onto the pi pico. 
1) hold down the button on the pico while its powered off
2) plug in the pico
3) let go of the button
4) your filemanager should pop up with an RP-RP2 folder. 
5) drag and drop or copy over the .uf2 file
6) unplug and repower the pico
7) A new pop up will show you the file structure of the pico.You should see a libs folder
8) place any dependencies or libraries that your devices require. For example the LSM6DS33 neews busio, register, and the LSM6D libraries in the lib folder. 
9) These libraries can be found in the `adafruit-circuitpython-bundle-8.x-mpy-20231029/lib/` folder. 
10) Write your main.py code using Thonny, a IDE for writing micropython and CircuitPython. Hit the green play button to flash and execute the code on the pico
11) Upload code.py to have a auto start function of the code upon powerup. 


## Further Developement

The next stages of developement are to:
1) test further sensors

## Lib

The library folder containts all of the libraries necessary to run our code.py program

## Other Folder
Each folder that is called IMU or GPS for example tests the specific code for that module. 
