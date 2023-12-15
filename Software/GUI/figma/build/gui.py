
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/tk/Projects/SD2/Software/GUI/figma/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("577x594")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 594,
    width = 577,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    42.0,
    55.0,
    207.0,
    114.0,
    fill="#000000",
    outline="")

canvas.create_text(
    192.0,
    304.0,
    anchor="nw",
    text="Testing output",
    fill="#000000",
    font=("Inter", 12 * -1)
)
window.resizable(False, False)
window.mainloop()