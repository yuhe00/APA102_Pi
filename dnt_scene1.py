#!/usr/bin/env python3

import time
import math
import random

import apa102

NUM_LEDS = 44

def main():
    try:
        strip = apa102.APA102(num_led = NUM_LEDS,
                              global_brightness = 140,
                              mosi = 10,
                              sclk = 11,
                              order = 'rbg')

        trains = [] # Trains are (length, position, speed)

        currentTime = time.time() # In seconds

        while True:
            deltaTime = time.time() - currentTime
            currentTime = time.time()

            trains = list(map(lambda (l, p, s): (l, p + deltaTime * s, s), trains))
            trains = list(filter(lambda (l, p, _): (int(p * (NUM_LEDS - 1)) - l) < NUM_LEDS, trains))

            if random.random() > 0.998:
                length = random.randrange(0, 10)
                speed = random.randrange(2.0, 5.0)
                trains.append((length, 0, speed))

            for i in range(0, (NUM_LEDS - 1)):
                strip.set_pixel(i, 255, 255, 255, 255)

            for (l, p, s) in trains:
                for i in range(0, l):
                    index = NUM_LEDS - int(p * NUM_LEDS)
                    strip.set_pixel(min(index + i, NUM_LEDS - 1), 0, 0, 0, 0)

            strip.show();

            time.sleep(1 / 60)

    except KeyboardInterrupt:
        print('Interrupted...')

    strip.clear_strip()
    strip.cleanup()

if __name__ == "__main__":
    main()
