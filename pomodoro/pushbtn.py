from micropython import const
from machine import Pin
import time

class PushButton:
    def __init__(self, pin):
        self.pin = pin
        self._value = 0
        self.press_count = 0

    def update(self):
        # (needs to be called repeatedly)
        self._value = ((self._value << 1) | bool(self.pin())) & 0x1fff
        if self._value == 0x1000:
            self.press_count += 1
            return True
        return False
