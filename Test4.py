import board
import neopixel
import time

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5

led_strip = neopixel.NeoPixel(board.DATA, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

def simple_led_pattern():
    # Define the colors for the pattern
    color1 = (0, 255, 0)   # Green
    color2 = (0, 0, 255)   # Blue
    color3 = (255, 0, 0)   # Red

    # Define the number of repetitions for the pattern
    num_repetitions = 3

    try:
        while True:
            # Loop through each repetition of the pattern
            for rep in range(num_repetitions):
                # Show color1 on all LEDs for 0.2 seconds
                led_strip.fill(color1)
                led_strip.show()
                time.sleep(0.2)

                # Show color2 on all LEDs for 0.2 seconds
                led_strip.fill(color2)
                led_strip.show()
                time.sleep(0.2)

                # Show color3 on all LEDs for 0.2 seconds
                led_strip.fill(color3)
                led_strip.show()
                time.sleep(0.2)

            # Pause for 1 second between repetitions
            time.sleep(1)

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

# Call the function to run the LED pattern
simple_led_pattern()

