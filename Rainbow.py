import board
import neopixel
import time
import random

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5

led_strip = neopixel.NeoPixel(board.DATA, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)  # Use the appropriate pin

def rainbow_colors_pattern():
    try:
        while True:
            # Create a list of rainbow colors
            rainbow_colors = [
                (148, 0, 211),  # Violet
                (75, 0, 130),   # Indigo
                (0, 0, 255),    # Blue
                (0, 255, 0),    # Green
                (255, 255, 0),  # Yellow
                (255, 127, 0),  # Orange
                (255, 0, 0)     # Red
            ]
            
            # Display the rainbow colors on the LED strip
            for color in rainbow_colors:
                for i in range(NUM_LEDS):
                    led_strip[i] = color
                led_strip.show()
                time.sleep(0.1)  # Adjust the delay as desired
            
            # Turn off the LEDs before the next pattern
            led_strip.fill((0, 0, 0))
            led_strip.show()
            time.sleep(0.1)

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

# Call the function to run the rainbow colors pattern
rainbow_colors_pattern()
