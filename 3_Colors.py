import board
import neopixel
import time
import random

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5

led_strip = neopixel.NeoPixel(board.D18, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)  # Use the appropriate pin

def limited_color_pattern():
    try:
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue

        while True:
            for color in colors:
                for i in range(NUM_LEDS):
                    led_strip[i] = color

                # Show the pattern on the LED strip
                led_strip.show()

                # Delay before generating the next pattern
                time.sleep(1)

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

# Call the function to run the limited color pattern
limited_color_pattern()
