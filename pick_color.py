import serial


class Color_Picker():

    def __init__(self, port='/dev/ttyUSB0'):
        self.port = serial.Serial(port)

    def send(self, data):
        self.port.write(data.encode())

    def red_color(self):
        self.send('237, 28, 28')  # RGB - 237 28 28

    def orange_color(self):
        self.send('255, 126, 28')  # RGB - 255 126 28

    def yellow_color(self):
        self.send('255, 228, 28')  # RGB - 255 228 28

    def green_color(self):
        self.send('42, 178, 37')  # RGB - 42 178 37

    def blue_color(self):
        self.send('24, 86, 178')  # RGB - 24 86 178

    def violet_color(self):
        self.send('128, 18, 165')  # RGB - 128 18 165

    def custom_color(self, r_color, g_color, b_color):
        self.send('r_color, g_color, b_color')


if __name__ == '__main__':
    port = input("Serial Port [/dev/ttyUSB0]:")
    if port:
        drive = Color_Picker(port)
    else:
        drive = Color_Picker()