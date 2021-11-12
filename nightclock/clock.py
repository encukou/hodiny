from machine import Pin
from time import sleep
import time
import network
import ntptime
from machine import idle

DST_START = 3, 28, 3
DST_END = 31, 10, 3

with open('settings.txt') as f:
    # The file settings.txt must have wifi and NTP config on 3 lines:
    SSID = f.readline().strip()
    PASSWORD = f.readline().strip()
    ntptime.host = f.readline().strip()

def cettime():
    # From https://forum.micropython.org/viewtopic.php?f=2&t=4034
    # Micropython esp8266
    # This code returns the Central European Time (CET) including daylight saving
    # Winter (CET) is UTC+1H Summer (CEST) is UTC+2H
    # Changes happen last Sundays of March (CEST) and October (CET) at 01:00 UTC
    # Ref. formulas : http://www.webexhibits.org/daylightsaving/i.html
    #                 Since 1996, valid through 2099
    year = time.localtime()[0]       #get current year
    HHMarch   = time.mktime((year,3 ,(31-(int(5*year/4+4))%7),1,0,0,0,0,0)) #Time of March change to CEST
    HHOctober = time.mktime((year,10,(31-(int(5*year/4+1))%7),1,0,0,0,0,0)) #Time of October change to CET
    now=time.time()
    if now < HHMarch :               # we are before last sunday of march
        cet=time.localtime(now+3600) # CET:  UTC+1H
    elif now < HHOctober :           # we are before last sunday of october
        cet=time.localtime(now+7200) # CEST: UTC+2H
    else:                            # we are after last sunday of october
        cet=time.localtime(now+3600) # CET:  UTC+1H
    return(cet)

def rot180(src):
    """Oh no, I built the thing upside down! Rotate in software"""
    a = bool(src & 0b10000000)
    b = bool(src & 0b01000000)
    c = bool(src & 0b00100000)
    d = bool(src & 0b00010000)
    e = bool(src & 0b00001000)
    f = bool(src & 0b00000100)
    g = bool(src & 0b00000010)
    p = bool(src & 0b00000001)
    return (d<<7) | (e<<6) | (f<<5) | (a<<4) | (b<<3) | (c<<2) | (g<<1) | p

digits = {
    n: rot180(b) for n, b in {
    0: 0b11111100,
    1: 0b01100000,
    2: 0b11011010,
    3: 0b11110010,
    4: 0b01100110,
    5: 0b10110110,
    6: 0b10111110,
    7: 0b11100000,
    8: 0b11111110,
    9: 0b11110110,
    "c": 0b10011100,
    "o": 0b00111010,
    "n": 0b00101010,
    "t": 0b00011110,
    "p": 0b11001110,
    "a": 0b11101110,
    " ": 0b00000000,
    "_": 0b00010000,
    "-": 0b00000010,
    "~": 0b10000000,
    "⠁": 0b10000000,
    "⠂": 0b01000000,
    "⠄": 0b00100000,
    "⠠": 0b00010000,
    "⠐": 0b00001000,
    "⠈": 0b00000100,
}.items()}

ser = Pin(15, Pin.OUT)  # D8
rclk = Pin(4, Pin.OUT)  # D2
srclk = Pin(2, Pin.OUT)  # D4
srclr_ = Pin(14, Pin.OUT)  # D5
button = Pin(0, Pin.IN)  # D3
digit_pins = [
    # Oh no, I built the thing upside down! Rhese are reversed.
    Pin(5, Pin.OUT),  # D1
    Pin(13, Pin.OUT),  # D7
    Pin(12, Pin.OUT),  # D6
    Pin(16, Pin.OUT),  # D0
]

rclk(0)
srclk(1)
srclr_(0)
srclr_(1)

def show_bytes(bytes):
    prev_pin = digit_pins[-1]
    for current_pin, byte in zip(digit_pins, bytes):
        rclk(0)
        for b in range(8):
            srclk(0)
            ser((byte >> b) & 1)
            srclk(1)
        prev_pin(1)
        rclk(1)
        current_pin(0)
        prev_pin = current_pin

def display_off():
    for pin in digit_pins:
        pin(1)

display_off()

def show_str(string):
    show_bytes(digits[c] for c in string)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
show_str("can-")
wlan.scan()
n_tries = 0
print('Connecting...')
while not wlan.isconnected():
    if n_tries % 100 == 0:
        wlan.connect(SSID, PASSWORD)
        idle()
    start = time.ticks_ms() # get millisecond counter
    sleep(0.1)
    show_str("⠁⠁⠁⠁⠁⠂⠄⠠⠐⠈"[n_tries % 10])
    n_tries += 1
print('Connected')

display_off()

def ntp_sync():
    print('NTP sync...')
    global NEXT_SYNC
    n_tries = 0
    while True:
        try:
            ntptime.settime()
            break
        except OSError:
            start = time.ticks_ms() # get millisecond counter
            while True:
                delta = time.ticks_diff(time.ticks_ms(), start)
                if delta > 1000:
                    break
                show_str("ntp" + "_-~"[n_tries % 3])
            n_tries += 1

    yr, mo, dy, hr, mn, sc, wday, yday = cettime()
    NEXT_SYNC = yr, mo, dy, hr + 1
    print('synced')

ntp_sync()
display_off()

while True:
    if not button():
        while True:
            yr, mo, dy, hr, mn, sc, wday, yday = localtime = cettime()
            if button():
                break
            digs = (
                digits[(hr // 10) % 10] | (sc & 1),
                digits[hr % 10],
                digits[(mn // 10) % 10] | 1,
                digits[mn % 10],
            )
            show_bytes(digs)
        display_off()
        if localtime > NEXT_SYNC:
            ntp_sync()
    idle()

