import board
import neopixel
import time
import random

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5

led_strip = neopixel.NeoPixel(board.Data, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)  # Use the appropriate pin

def random_color_pattern():
    try:
        while True:
            for i in range(NUM_LEDS):
                # Generate a random color
                random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                # Set the current LED to the random color
                led_strip[i] = random_color

            # Show the pattern on the LED strip
            led_strip.show()

            # Delay before generating the next pattern
            time.sleep(1)

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

# Call the function to run the random color pattern
random_color_pattern()
