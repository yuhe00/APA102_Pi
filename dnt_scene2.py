#!/usr/bin/env python3

import time
import math
import random

import apa102

NUM_LEDS = 37

def main():
    try:
        strip = apa102.APA102(num_led = NUM_LEDS,
                              global_brightness = 255,
                              mosi = 10,
                              sclk = 11,
                              order = 'rbg')

        currentTime = time.time() # In seconds

        while True:
            deltaTime = time.time() - currentTime
            currentTime = time.time()

            for i in range(0, (NUM_LEDS - 1)):
                n = int(((math.sin(currentTime) + 1) / 2) * 64) + 32
                strip.set_pixel(i, n, n, n, n)

            strip.show();

            time.sleep(1 / 60)

    except KeyboardInterrupt:
        print('Interrupted...')

    strip.clear_strip()
    strip.cleanup()

if __name__ == "__main__":
    main()
