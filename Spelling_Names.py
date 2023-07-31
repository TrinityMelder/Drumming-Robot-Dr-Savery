import board
import neopixel
import time

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5

led_strip = neopixel.NeoPixel(board.DATA, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

def display_name_pattern(name, color, duration=0.3):
    # Define the colors
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    purple = (255, 0, 255)
    cyan = (0, 255, 255)
    white = (255, 255, 255)
    off = (0, 0, 0)

    # Dictionary mapping each letter to its LED representation
    letter_leds = {
        'A': [0, 1, 2, 3, 4, 15, 27, 39, 52, 64, 75, 87, 88, 89, 90, 91, 92, 93, 94, 95],
        'B': [0, 1, 2, 3, 4, 5, 15, 27, 39, 52, 64, 75, 87, 88, 89, 90, 91, 92, 93, 94, 95],
        # Add more letters as needed...
    }

    try:
        while True:
            # Display each letter in the name
            for letter in name:
                # Check if the letter is in the dictionary
                if letter.upper() in letter_leds:
                    leds_to_light = letter_leds[letter.upper()]

                    # Light up the LEDs corresponding to the letter with the specified color
                    for led_index in leds_to_light:
                        led_strip[led_index] = color

                    # Show the pattern on the LED strip
                    led_strip.show()

                    # Pause for the specified duration
                    time.sleep(duration)

                    # Turn off the LEDs before displaying the next letter
                    for led_index in leds_to_light:
                        led_strip[led_index] = off

                    # Pause for a short duration between letters
                    time.sleep(0.1)

                else:
                    # If the letter is not in the dictionary, skip it
                    continue

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill(off)
        led_strip.show()

# Call the function to spell out the given name in the pattern with a specific color and duration
name_to_spell = "ADAFRUIT"
name_color = (255, 0, 255)  # Purple
pattern_duration = 0.3
display_name_pattern(name_to_spell, name_color, pattern_duration)
