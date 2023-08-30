import board
import neopixel
import time
import random

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5

led_strip = neopixel.NeoPixel(board.Data, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)  # Use the appropriate pin

def color_sequence_pattern():
    try:
        while True:
            for i in range(NUM_LEDS):
                red = (255, 0, 0)
                green = (0, 255, 0)
                blue = (0, 0, 255)

                if i % 3 == 0:
                    led_strip[i] = red
                    led_strip[i + 1] = green
                    led_strip[i + 2] = blue
                elif i % 3 == 1:
                    led_strip[i] = green
                    led_strip[i + 1] = blue
                    led_strip[i + 2] = red
                else:
                    led_strip[i] = blue
                    led_strip[i + 1] = red
                    led_strip[i + 2] = green

            # Show the pattern on the LED strip
            led_strip.show()

            # Delay before generating the next pattern
            time.sleep(1)

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

# Call the function to run the color sequence pattern
color_sequence_pattern()
