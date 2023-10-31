import board
import neopixel
import time
import random

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5
CHASE_SIZE = 5
COMET_LENGTH = 5
TRAIL_LENGTH = 10

# Use the appropriate pin
led_strip = neopixel.NeoPixel(board.DATA, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)

def random_color_pattern():
    for i in range(NUM_LEDS):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        led_strip[i] = random_color
        led_strip.show()
        time.sleep(0.05)

def rainbow_colors_pattern():
    rainbow_colors = [
        (148, 0, 211),  # Violet
        (75, 0, 130),   # Indigo
        (0, 0, 255),    # Blue
        (0, 255, 0),    # Green
        (255, 255, 0),  # Yellow
        (255, 127, 0),  # Orange
        (255, 0, 0)     # Red
    ]

    for color in rainbow_colors:
        for i in range(NUM_LEDS):
            led_strip[i] = color
        led_strip.show()
        time.sleep(0.1)

    led_strip.fill((0, 0, 0))
    led_strip.show()
    time.sleep(0.01)

def single_led_purple_pattern():
    for i in range(NUM_LEDS):
        led_strip.fill((0, 0, 0))
        led_strip[i] = (128, 0, 128)  # Purple (adjust the RGB values as needed)
        led_strip.show()
        time.sleep(0.001)
        led_strip[i] = (0, 0, 0)
        led_strip.show()
        time.sleep(0.001)
        

def chaser_purple_pattern():
    for i in range(NUM_LEDS):
        led_strip.fill((0, 0, 0))

        for j in range(CHASE_SIZE):
            led_index = (i + j) % NUM_LEDS
            led_strip[led_index] = (128, 0, 128)  # Purple (adjust the RGB values as needed)

        led_strip.show()
        time.sleep(0.05)

# Incorporate the comet_pattern function
def comet_pattern():
    for i in range(NUM_LEDS + COMET_LENGTH):
                led_strip.fill((0, 0, 0))  # Clear all LEDs

                if i < NUM_LEDS:
                    # Calculate the comet color based on its position
                    comet_color = (255, 0, 165)  # Purple (You can adjust the RGB values)

                    # Light up the comet
                    for j in range(COMET_LENGTH):
                        led_index = i - j
                        led_strip[led_index] = comet_color

                    # Create the fading trail
                    for j in range(TRAIL_LENGTH):
                        led_index = i - COMET_LENGTH - j
                        fade_factor = (TRAIL_LENGTH - j) / TRAIL_LENGTH
                        faded_color = (
                            int(255 * fade_factor),  # Darker Orange (Red component)
                            int(100 * fade_factor),  # Darker Orange (Green component)
                            0  # Darker Orange (Blue component)
                        )
                        led_strip[led_index] = faded_color

                led_strip.show()
                time.sleep(0.05)  # Adjust the speed of the comet movement

# Call the functions sequentially
patterns = [
    random_color_pattern,
    rainbow_colors_pattern,
    single_led_purple_pattern,
    chaser_purple_pattern,
    comet_pattern,
]

for pattern in patterns:
    pattern()
