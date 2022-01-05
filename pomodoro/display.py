from micropython import const
from machine import SPI
import time

REG_LAST_DIGIT = 0x8
REG_DECODEMODE = 0x9
REG_INTENSITY = 0xA
REG_SCANLIMIT = 0xB
REG_SHUTDOWN = 0xC
REG_DISPLAYTEST = 0xF

# Pin bits:  111      aaa
#           6   2    f   b
#           6   2    f   b
#            777      ggg
#           5   3    e   c
#           5   3    e   c
#            444  0   ddd  p

alphabet = {
    ' ': 0b00000000,
    '0': 0b01111110,
    '1': 0b00110000,
    '2': 0b01101101,
    '3': 0b01111001,
    '4': 0b00110011,
    '5': 0b01011011,
    '6': 0b01011111,
    '7': 0b01110000,
    '8': 0b01111111,
    '9': 0b01111011,
    '-': 0b00000001,
    'a': 0b01110111,
    'c': 0b00001101,
    'č': 0b01001101,
    'e': 0b01001111,
    'h': 0b00010111,
    'j': 0b00111100,
    'l': 0b00001110,
    'n': 0b00010101,
    'o': 0b00011101,
    'r': 0b00000101,
    's': 0b01011011,
    'v': 0b00011100,
    'z': 0b01101101,
}
DOT = const(0b10000000)
BADSYM = const(0b01000001)

class Display:
    def __init__(self, cs_pin, mosi_pin, sck_pin, baudrate=10_000):
        self.cs_pin = cs_pin
        self.spi = SPI(1)
        self.spi.deinit()
        self.spi.init(
            1, baudrate=baudrate, polarity=0, phase=0,
            mosi=mosi_pin, sck=sck_pin,
        )
        self.baudrate = baudrate
        self.reset()

    def reset(self):
        self.buf = [0] * 8
        self.prev_buf = [0xff] * 8

        self.command(REG_SHUTDOWN, 0)
        self.command(REG_DISPLAYTEST, 0)
        self.command(REG_SCANLIMIT, 7)
        self.command(REG_DECODEMODE, 0)
        self.command(REG_SHUTDOWN, 1)
        self.command(REG_INTENSITY, 1)
        self.flush()

    def flush(self):
        for i in range(8):
            if self.prev_buf[i] != self.buf[i]:
                self.write([REG_LAST_DIGIT - i, self.buf[i]])
                self.prev_buf[i] = self.buf[i]

    def write(self, data):
        self.cs_pin(0)
        self.spi.write(bytes(data))
        self.cs_pin(1)

    def command(self, register, data):
        self.write([register, data])

    def put_text(self, text, start=0, clear_rest=True, add=False, flush=True):
        i = start - 1
        for letter in text:
            if letter == '.':
                self.buf[i] |= DOT
            else:
                if i >= 7:
                    break
                i += 1
                if not add:
                    self.buf[i] = 0
                self.buf[i] |= alphabet.get(letter, BADSYM)
        else:
            if clear_rest:
                for i in range(i + 1, 8):
                    self.buf[i] = 0
        if flush:
            self.flush()
