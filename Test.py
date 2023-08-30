import board
import neopixel
import time

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5

led_strip = neopixel.NeoPixel(board.D18, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)  # Use the appropriate pin

def single_led_red_pattern():
    try:
        for i in range(NUM_LEDS):
            # Turn on the current LED in red
            led_strip.fill((0, 0, 0))  # Turn off all LEDs
            led_strip[i] = (255, 0, 0)  # Red
            led_strip.show()
            time.sleep(1)  # LED on time
            
            # Turn off the current LED
            led_strip[i] = (0, 0, 0)  # Turn off the current LED
            led_strip.show()
            time.sleep(0.1)  # Delay between LEDs

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

# Call the function to run the single LED red pattern
single_led_red_pattern()
