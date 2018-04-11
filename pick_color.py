"""
Rowan D'Ausilio
LED Lightstrip project
"""

import serial

"""
debate on just a large switch statement for color change? 
prefix b is required when writing to serial
"""


class Color_Picker():

    def __init__(self, port='/dev/ttyUSB0'):
        self.port = serial.Serial(port)

    def send(self, data):
        self.port.write(data.encode())

    def red_color(self, rv, gv, bv):
        self.send("B" + rv + gv + bv)  # RGB - 237 28 28

    def orange_color(self, rv, gv, bv):
        self.send("B" + rv + gv + bv)  # RGB - 255 126 28

    def yellow_color(self, rv, gv, bv):
        self.send("B" + rv + gv + bv)  # RGB - 255 228 28

    def green_color(self, rv, gv, bv):
        self.send("B" + rv + gv + bv)  # RGB - 42 178 37

    def blue_color(self, rv, gv, bv):
        self.send("B" + rv + gv + bv)  # RGB - 24 86 178

    def violet_color(self, rv, gv, bv):
        self.send("B" + rv + gv + bv)  # RGB - 128 18 165

    # def custom_color(self, r_color, g_color, b_color):
    # self.send('r_color, g_color, b_color')


if __name__ == '__main__':
    port = input("Serial Port [/dev/ttyUSB0]:")
    if port:
        drive = Color_Picker(port)
    else:
        drive = Color_Picker()

    while True:
        choice = input("What color do you want the light strip to change to?")
        choice = choice.upper()
        if choice == "R":
            drive.red_color(237, 28, 28)
        if choice == "O":
            drive.orange_color(225, 126, 28)
        if choice == "Y":
            drive.yellow_color(255, 228, 28)
        if choice == "G":
            drive.green_color(42, 178, 37)
        if choice == "BLUE":
            drive.blue_color(24, 86, 178)
        if choice == "V":
            drive.violet_color(128, 18, 165)
