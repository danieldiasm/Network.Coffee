# Push Button Module
from machine import Pin

class Button:

    def __init__(self, label, handler, gpio_pin:int=39) -> None:
        self.button = None
        self.button_label = label
        self.button_gpio_pin = gpio_pin
        self.button_state = False
        self.handler = handler

    def setup_button(self):
        self.button = Pin(self.button_gpio_pin, Pin.IN, Pin.PULL_UP)
        self.button.irq(trigger=Pin.IRQ_FALLING, handler=self.handler)
    