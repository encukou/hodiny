from micropython import const
from machine import Pin

# Rotary encoder transition table from:
#   https://github.com/MikeTeachman/micropython-rotary
# The MIT License (MIT)
# Copyright (c) 2020 Mike Teachman
# https://opensource.org/licenses/MIT
# after Ben Buxton's implementation:
#   http://www.buxtronix.net/2011/10/rotary-encoders-done-properly.html

# Rotary Encoder States
_R_START = const(0x0)
_R_CW_1 = const(0x1)
_R_CW_2 = const(0x2)
_R_CW_3 = const(0x3)
_R_CCW_1 = const(0x4)
_R_CCW_2 = const(0x5)
_R_CCW_3 = const(0x6)
_R_ILLEGAL = const(0x7)
_R_MASK = const(0x7)

_DIR_CW = const(0x10)  # Clockwise step
_DIR_CCW = const(0x20)  # Counter-clockwise step
_DIR_MASK = const(0xf0)

_transition_table = [
    # |------------- NEXT STATE -------------|            |CURRENT STATE|
    # CLK/DT    CLK/DT     CLK/DT    CLK/DT
    #   00        01         10        11
    [_R_START, _R_CCW_1, _R_CW_1,  _R_START],             # _R_START
    [_R_CW_2,  _R_START, _R_CW_1,  _R_START],             # _R_CW_1
    [_R_CW_2,  _R_CW_3,  _R_CW_1,  _R_START],             # _R_CW_2
    [_R_CW_2,  _R_CW_3,  _R_START, _R_START | _DIR_CW],   # _R_CW_3
    [_R_CCW_2, _R_CCW_1, _R_START, _R_START],             # _R_CCW_1
    [_R_CCW_2, _R_CCW_1, _R_CCW_3, _R_START],             # _R_CCW_2
    [_R_CCW_2, _R_START, _R_CCW_3, _R_START | _DIR_CCW],  # _R_CCW_3
    [_R_START, _R_START, _R_START, _R_START],             # _R_ILLEGAL
]

class Rotary:
    def __init__(self, pin_a, pin_b, pin_btn):
        self._encoder_state = _R_START

        self.value = 0
        self.pressed_value = 0
        self.changed = 0

        self.pin_a = pin_a
        self.pin_b = pin_b
        self.pin_btn = pin_btn

        pin_a.irq(self.encoder_irq, Pin.IRQ_RISING|Pin.IRQ_FALLING)
        pin_b.irq(self.encoder_irq, Pin.IRQ_RISING|Pin.IRQ_FALLING)

    def encoder_irq(self, val):
        encoder_data = (self.pin_a() << 1) | self.pin_b()
        self._encoder_state = (
            _transition_table[self._encoder_state][encoder_data]
        )
        if self._encoder_state & _DIR_MASK: 
            if self.pin_btn():
                if self._encoder_state & _DIR_CW: 
                    self.value += 1
                else:
                    self.value -= 1
            else:
                if self._encoder_state & _DIR_CW: 
                    self.pressed_value += 1
                else:
                    self.pressed_value -= 1
            self.changed = 1
            self._encoder_state &= _R_MASK

    def reset(self):
        self.value = self.pressed_value = self.changed = 0
