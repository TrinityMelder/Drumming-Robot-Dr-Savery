import board
import neopixel
import time

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 1

led_strip = neopixel.NeoPixel(board.DATA, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

def clock_based_led_pattern():
    try:
        while True:
            # Get the current time in seconds
            current_time = time.localtime()
            seconds = current_time.tm_sec

            # Calculate the color based on the seconds
            red = min(seconds * 10, 255)
            green = min((60 - seconds) * 10, 255)
            blue = 0

            # Fill the LED strip with the calculated color
            for i in range(NUM_LEDS):
                led_strip[i] = (red, green, blue)

            led_strip.show()
            time.sleep(1)  # Update the display every second

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

# Call the function to run the LED pattern
clock_based_led_pattern()
