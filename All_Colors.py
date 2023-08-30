import board
import neopixel
import time
import random

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5
NUM_CYCLES = 5

led_strip = neopixel.NeoPixel(board.D18, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)  # Use the appropriate pin

def random_color_pattern():
    try:
        for _ in range(NUM_CYCLES):
            for i in range(NUM_LEDS):
                # Generate a random color
                random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                # Turn on the current LED with the random color
                led_strip.fill((0, 0, 0))  # Turn off all LEDs
                led_strip[i] = random_color
                led_strip.show()
                time.sleep(1)  # LED on time

                # Turn off the current LED
                led_strip[i] = (0, 0, 0)  # Turn off the current LED
                led_strip.show()
                time.sleep(0.1)  # Delay between LEDs
            
            # Delay between cycles
            time.sleep(1)

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

# Call the function to run the random color pattern
random_color_pattern()
