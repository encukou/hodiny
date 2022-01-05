from machine import Pin
from network import WLAN
from time import sleep, ticks_ms, ticks_diff
import machine
import neopixel

from rotary import Rotary
from display import Display
from pushbtn import PushButton

MISO_PIN = 12
MOSI_PIN = 13
SCK_PIN = 14
CS_PIN = 27
ROT_PIN_A = 25
ROT_PIN_B = 26
ROT_PIN_BTN = 33
RGB_PIN = 32

START_BTN_PIN = 4
PAUSE_BTN_PIN = 17
TIME5_BTN_PIN = 16
TIME25_BTN_PIN = 5

RGB_NUM = 22

WLAN(0).active(0)
WLAN(1).active(0)

cs = Pin(CS_PIN, Pin.OUT, value=1)

rotary = Rotary(
    pa := Pin(ROT_PIN_A, Pin.IN, Pin.PULL_UP),
    Pin(ROT_PIN_B, Pin.IN, Pin.PULL_UP),
    Pin(ROT_PIN_BTN, Pin.IN, Pin.PULL_UP),
)

display = Display(
    Pin(CS_PIN, Pin.OUT),
    Pin(MOSI_PIN, Pin.OUT),
    Pin(SCK_PIN, Pin.OUT),
    baudrate=100_000,
)

start_btn = PushButton(Pin(START_BTN_PIN, Pin.IN, Pin.PULL_UP))
time5_btn = PushButton(Pin(TIME5_BTN_PIN, Pin.IN, Pin.PULL_UP))
time25_btn = PushButton(Pin(TIME25_BTN_PIN, Pin.IN, Pin.PULL_UP))
pause_btn = PushButton(Pin(PAUSE_BTN_PIN, Pin.IN, Pin.PULL_UP))

np = neopixel.NeoPixel(Pin(RGB_PIN, Pin.OUT), RGB_NUM)

def timerepr(time):
    if time >= 36000:
        return f'{time // 3600:3}h.'
    elif time >= 3600:
        return f'{time // 3600}h.{((time // 60) % 60):02}'
    else:
        return f'{time // 60:2}.{time % 60:02}'

class State:
    def __init__(self):
        self._started = False
        self._start_time = None
        self._total_time = 0
        self._total_time_changed()

    def _total_time_changed(self):
        self._total_time_repr = timerepr(self._total_time)

    def add_time(self, minutes):
        self._total_time += minutes * 60
        self._total_time_changed()
        if not self._started:
            self.start()

    def start(self):
        self._start_time = ticks_ms()
        self._started = True

    def countdown_time(self):
        if self._start_time is None:
            return 0
        else:
            return (
                self._total_time
                - ticks_diff(ticks_ms(), self._start_time) // 1000
            )

    def _elapsed_repr(self):
        if self._start_time is None:
            return '    '
        return timerepr(self.countdown_time())

    def handle_rotary(self, rotary):
        self._total_time += rotary.value * 60
        self._total_time_changed()
        rotary.reset()

    def fill_np(self, np):
        np.fill((0, 0, 0))
        if self.countdown_time() < 0 and (ticks_ms() // 50 % 2) < 1:
            np.fill((255, 255, 255))
        return

        if self._start_time is None:
            pass
        elif self._total_time == 0:
            pass
        else:
            n = RGB_NUM * self.countdown_time() / self._total_time
            i = 0
            for i in range(int(n)):
                np[i] = 255, 255, 255
            if i + 1 < RGB_NUM:
                np[i + 1] = (int((n%1) * 255), ) * 3

    def __str__(self):
        if self._start_time is None:
            return '    ' + self._total_time_repr
        else:
            return self._elapsed_repr()

state = State()

print('!')
display.put_text('0123.4567.89')
display.put_text('89')
display.reset()
print('u')
while True:
    if time5_btn.update():
        state.add_time(5)
    if time25_btn.update():
        state.add_time(25)
    state.handle_rotary(rotary)
    display.put_text(str(state))
    state.fill_np(np)
    np.write()
    sleep(0.001)
print('.')
