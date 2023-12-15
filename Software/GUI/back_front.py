
import tkinter as tk
import serial

def update_gui(data_dict):
    for key, entry_var in entry_vars.items():
        entry_var.set(f"{key}: {data_dict.get(key, '')}")

def toggle_read_uart():
    global reading_uart
    if reading_uart:
        stop_read_uart()
    else:
        start_read_uart()

def start_read_uart():
    global reading_uart
    reading_uart = True
    read_button.config(text="Stop Reading")
    
    try:
        ser = serial.Serial(serial_port, baud_rate, timeout=1)
        print(f"Reading UART data from {serial_port}...")

        while reading_uart:
            data = ser.readline().decode('utf-8').strip()
            if data:
                if data[0] == "/":
                    data = data[2:len(data)-1]
                    data_list = data.split(',')
                    data_dict = dict(zip(labels, data_list))
                    
                    update_gui(data_dict)
                    root.update()

    except serial.SerialException as e:
        print(f"Error: {e}")
        stop_read_uart()

def stop_read_uart():
    global reading_uart
    reading_uart = False
    read_button.config(text="Start Reading")

def close_application():
    root.destroy()

if __name__ == "__main__":
    serial_port = '/dev/ttyACM0'
    baud_rate = 115200

    labels = [
        "Year", "Month", "Day", "Hour", "Minute", "Second", "Satellites", "Latitude", "Longitude",
        "Elevation", "X Acceleration", "Y Acceleration", "Z Acceleration",
        "X Magnetic", "Y Magnetic", "Z Magnetic", "X Gyro", "Y Gyro", "Z Gyro"
    ]

    reading_uart = False

    root = tk.Tk()
    root.title("UART Data Display")
    
    # Style
    root.geometry("600x400")
    root.configure(bg="#F0F0F0")

    entry_vars = {}
    for key in labels:
        entry_var = tk.StringVar()
        entry_var.set(f"{key}: ")
        entry_vars[key] = entry_var

        entry = tk.Entry(root, textvariable=entry_var, state=tk.DISABLED, disabledforeground="black")
        entry.pack(pady=5, padx=150)

    read_button = tk.Button(root, text="Start Reading", command=toggle_read_uart)
    read_button.pack(pady=10)

    close_button = tk.Button(root, text="Close", command=close_application)
    close_button.pack(pady=10)

    root.mainloop()
