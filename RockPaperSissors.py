# generated by mBlock5 for HaloCode
# codes make you happy

import event, halo, time, random
import time
# initialize variables
LED = 0
Sound = 0
Random = 0
Delay = 0

@event.button_pressed
def on_button_pressed():
    global LED, Sound, Random, Delay
    Delay = 0.06
    Screen_Into()
    while not halo.button.is_pressed():
      Sound = halo.microphone.get_loudness("maximum")
      if Sound > 20:
        Countdown()
        Random = random.randint(1, 3)
        if Random == 1:
          Rock()

        if Random == 2:
          Paper()

        if Random == 3:
          Sissors()

        halo.led.off_all()
        time.sleep(1)

    halo.led.off_all()

def Screen_Into():
    global LED, Sound, Random, Delay
    Rock()
    Paper()
    Sissors()
    halo.led.off_all()

def Countdown():
    global LED, Sound, Random, Delay
    for count in range(3):
      Rotate_LED()

    time.sleep(0.5)

def Rotate_LED():
    global LED, Sound, Random, Delay
    LED = 1
    for count2 in range(12):
      halo.led.show_single(LED, 0, 128, 0)
      time.sleep(0.01)
      halo.led.off_single((LED - 1))
      time.sleep(0.01)
      LED = LED + 1
      halo.led.off_single(12)

def Rock():
    global LED, Sound, Random, Delay
    halo.led.show_ring('orange orange orange black orange orange orange orange orange orange orange orange')
    time.sleep(float(Delay))
    halo.led.show_ring('orange orange orange orange black orange orange orange orange orange orange orange')
    time.sleep(float(Delay))
    halo.led.show_ring('orange orange orange orange orange black orange orange orange orange orange orange')
    time.sleep(float(Delay))
    halo.led.show_ring('orange orange orange orange orange orange black orange orange orange orange orange')
    time.sleep(float(Delay))
    halo.led.show_ring('orange orange orange orange orange orange orange black orange orange orange orange')
    time.sleep(float(Delay))
    halo.led.show_ring('orange orange orange orange orange orange black orange orange orange orange orange')
    time.sleep(float(Delay))
    halo.led.show_ring('orange orange orange orange orange black orange orange orange orange orange orange')
    time.sleep(float(Delay))
    halo.led.show_ring('orange orange orange orange black orange orange orange orange orange orange orange')
    time.sleep(float(Delay))
    halo.led.show_ring('orange orange orange black orange orange orange orange orange orange orange orange')
    time.sleep(float(Delay))
    halo.led.show_ring('orange orange orange orange orange orange orange orange orange orange orange orange')
    time.sleep(0.5)

def Paper():
    global LED, Sound, Random, Delay
    halo.led.show_ring('black white black black black black black white black black black black')
    time.sleep(float(Delay))
    halo.led.show_ring('white white black black black black white white black black black black')
    time.sleep(float(Delay))
    halo.led.show_ring('white white black black black white white white black black black white')
    time.sleep(float(Delay))
    halo.led.show_ring('white white black black white white white white black black white white')
    time.sleep(float(Delay))
    halo.led.show_ring('white white black white white white white white black white white white')
    time.sleep(float(Delay))
    halo.led.show_ring('white white white white white white white white white white white white')
    time.sleep(float(Delay))
    time.sleep(0.5)

def Sissors():
    global LED, Sound, Random, Delay
    for count3 in range(2):
      halo.led.show_ring('cyan black black black cyan cyan cyan cyan cyan cyan cyan cyan')
      time.sleep(float(Delay))
      halo.led.show_ring('black black black black black cyan cyan cyan cyan cyan cyan cyan')
      time.sleep(float(Delay))
      halo.led.show_ring('cyan black black black cyan cyan cyan cyan cyan cyan cyan cyan')
      time.sleep(float(Delay))
      halo.led.show_ring('cyan cyan black cyan cyan cyan cyan cyan cyan cyan cyan cyan')
      time.sleep(float(Delay))
      halo.led.show_ring('cyan cyan cyan cyan cyan cyan cyan cyan cyan cyan cyan cyan')
      time.sleep(float(Delay))
      halo.led.show_ring('cyan cyan black cyan cyan cyan cyan cyan cyan cyan cyan cyan')
      time.sleep(float(Delay))
      halo.led.show_ring('cyan black black black cyan cyan cyan cyan cyan cyan cyan cyan')
      time.sleep(float(Delay))