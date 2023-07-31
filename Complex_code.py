import board
import neopixel
import time
import random

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5

led_strip = neopixel.NeoPixel(board.DATA, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

def complex_led_pattern():
    # Define some colors
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    purple = (255, 0, 255)
    cyan = (0, 255, 255)
    white = (255, 255, 255)
    off = (0, 0, 0)

    try:
        while True:
            # Randomly select a color for the pattern
            colors = [red, green, blue, yellow, purple, cyan]
            random_color = random.choice(colors)

            # Randomly select the number of LEDs to light up in the pattern
            num_leds_to_light = random.randint(3, 10)

            # Randomly select the starting LED index for the pattern
            start_index = random.randint(0, NUM_LEDS - num_leds_to_light)

            # Light up the selected LEDs with the random color
            for i in range(num_leds_to_light):
                led_strip[start_index + i] = random_color

            # Show the pattern on the LED strip
            led_strip.show()

            # Randomly select the duration for the pattern to be displayed
            pattern_duration = random.uniform(0.2, 0.8)
            time.sleep(pattern_duration)

            # Turn off the LEDs for a short pause before the next pattern
            led_strip.fill(off)
            led_strip.show()
            time.sleep(0.1)

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill(off)
        led_strip.show()

# Call the function to run the LED pattern
complex_led_pattern()
