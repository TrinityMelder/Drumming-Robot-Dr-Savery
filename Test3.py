import board
import neopixel
import time

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5
CHASE_SIZE = 5

led_strip = neopixel.NeoPixel(board.Data, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)  # Use the appropriate pin

def chaser_pattern():
    try:
        while True:
            for i in range(NUM_LEDS):
                led_strip.fill((0, 0, 0))  # Clear all LEDs

                for j in range(CHASE_SIZE):
                    led_index = (i + j) % NUM_LEDS
                    led_strip[led_index] = (0, 255, 0)  # Green color

                led_strip.show()
                time.sleep(0.05)  # Adjust the speed of the chaser movement

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

# Call the function to run the chaser pattern
chaser_pattern()
