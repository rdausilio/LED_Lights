"""
Rowan D'Ausilio
LED Light strip project
"""

import serial

"""
debate on just a large switch statement for color change? 
"""


class Color_Picker():

    def __init__(self, port='/dev/ttyUSB1'):
        self.port = serial.Serial(port)

    def send(self, data):
        self.port.write(data.encode())

    def red_color(self, color):
        self.send("B" + color)  # RGB - 237 28 28

    def orange_color(self, color):
        self.send("B" + color)  # RGB - 255 126 28

    def yellow_color(self, color):
        self.send("B" + color)  # RGB - 255 228 28

    def green_color(self, color):
        self.send("B" + color)  # RGB - 42 178 37

    def blue_color(self, color):
        self.send("B" + color)  # RGB - 24 86 178

    def purple_color(self, color):
        self.send("B" + color)  # RGB - 128 18 165


if __name__ == '__main__':
    port = input("Serial Port [/dev/ttyUSB1]:")
    if port:
        color_boi = Color_Picker(port)
    else:
        color_boi = Color_Picker()

    while True:
        command = input("What do you want the color to be?")
        if color_boi == "red":
            color_boi.red_color('/red')
        if color_boi == "orange":
            color_boi.orange_color('/orange')
        if color_boi == "yellow":
            color_boi.yellow_color('/yellow')
        if color_boi == "green":
            color_boi.green_color('/green')
        if color_boi == "blue":
            color_boi.blue_color('/blue')
        if color_boi == "purple":
            color_boi.purple_color('/purple')