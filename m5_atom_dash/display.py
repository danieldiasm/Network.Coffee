# Display Module
from machine import Pin
from neopixel import NeoPixel

class DisplayError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Display:

    def __init__(self, pin:int=27, size:int=25) -> None:
        self.neo_pin = Pin(pin, Pin.OUT)
        self.size = size
        self.np = NeoPixel(self.neo_pin, self.size)


    def set_pixel(self, pixel:int, colour:tuple) -> None:
        if pixel >= 0 or pixel <= self.size:
            self.np[pixel] = colour


    def clear_display(self):
        self.blank = [(0,0,0) for i in range(self.size)]
        self.display_frame(self.blank)
        del(self.blank)


    def display(self):
        self.np.write()


    def display_frame(self, display_map:list):
        for i in range(self.size):
            self.set_pixel(i, display_map[i])
        self.display()


    def eval_display(self, data):
        try:
            frame_map = eval(data)

            if isinstance(frame_map, list) \
            and isinstance(frame_map[0], tuple) \
            and len(frame_map) == self.size:
                self.display_frame(frame_map)
            elif isinstance(frame_map, list) and "clear" == frame_map[0]:
                self.clear_display()
            else:
                raise DisplayError("Invalid Display Map")
        except Exception as e:
            return e