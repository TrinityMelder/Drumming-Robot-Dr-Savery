import board
import neopixel
import time
import random

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5
COMET_LENGTH = 5
TRAIL_LENGTH = 10

led_strip = neopixel.NeoPixel(board.Data, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)  # Use the appropriate pin

def comet_pattern():
    try:
        while True:
            for i in range(NUM_LEDS + COMET_LENGTH):
                led_strip.fill((0, 0, 0))  # Clear all LEDs

                if i < NUM_LEDS:
                    # Calculate the comet color based on its position
                    comet_color = (255, int(255 - i * (255 / NUM_LEDS)), 0)

                    # Light up the comet
                    for j in range(COMET_LENGTH):
                        led_index = i - j
                        led_strip[led_index] = comet_color

                    # Create the fading trail
                    for j in range(TRAIL_LENGTH):
                        led_index = i - COMET_LENGTH - j
                        fade_factor = (TRAIL_LENGTH - j) / TRAIL_LENGTH
                        faded_color = (
                            int(comet_color[0] * fade_factor),
                            int(comet_color[1] * fade_factor),
                            int(comet_color[2] * fade_factor)
                        )
                        led_strip[led_index] = faded_color

                led_strip.show()
                time.sleep(0.05)  # Adjust the speed of the comet movement

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

# Call the function to run the comet pattern
comet_pattern()
