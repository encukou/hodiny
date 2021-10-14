from machine import Pin
from time import sleep
import time
import network
import ntptime
from machine import idle

DST_START = 3, 28, 3
DST_END = 31, 10, 3

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

digits = {
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
    " ": 0b00000000,
    "_": 0b00010000,
    "-": 0b00000010,
    "~": 0b10000000,
}

ser = Pin(5, Pin.OUT)  # D1
rclk = Pin(4, Pin.OUT)  # D2
srclk = Pin(2, Pin.OUT)  # D4
srclr_ = Pin(14, Pin.OUT)  # D5
button = Pin(0, Pin.IN)  # D3

rclk(0)
srclk(1)
srclr_(0)
srclr_(1)

def push_bits(*bytes):
    rclk(0)
    for byte in bytes:
        for b in range(8):
            srclk(0)
            ser((byte >> b) & 1)
            srclk(1)
    rclk(1)

def show_bytes(bytes):
    mask = 0b01111111
    for byte in bytes:
        push_bits(mask, byte)
        mask >>= 1
        mask |= 0b10000000

def show_str(string):
    show_bytes(digits[c] for c in string)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
n_tries = 0
if not wlan.isconnected():
    wlan.connect('Tlapicky', '4a2ouska')
    while not wlan.isconnected():
        start = time.ticks_ms() # get millisecond counter
        while True:
            delta = time.ticks_diff(time.ticks_ms(), start)
            if delta > 100:
                break
            show_str("con" + "_-~"[n_tries % 3])
        n_tries += 1

show_str("    ")

def ntp_sync():
    global NEXT_SYNC
    ntptime.host = '192.168.1.1'
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

ntp_sync()
show_str("    ")

while True:
    if not button():
        while True:
            yr, mo, dy, hr, mn, sc, wday, yday = localtime = cettime()
            if button():
                break
            digs = (
                digits[(hr // 10) % 10],
                digits[hr % 10] | 1,
                digits[(mn // 10) % 10],
                digits[mn % 10] | (sc & 1),
            )
            show_bytes(digs)
        show_str("    ")
        if localtime > NEXT_SYNC:
            ntp_sync()
    idle()
