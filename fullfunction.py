import board
import neopixel
import time
import random

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5

def color_sequence_pattern(led_strip):
    try:
        while True:
            for i in range(NUM_LEDS):
                led_strip.fill((0, 0, 0))  # Clear all LEDs

                # Define the new color sequence (Purple)
                sequence = [(128, 0, 128), (128, 0, 128), (128, 0, 128)]  # Purple color

                for j in range(3):
                    led_index = (i + j) % NUM_LEDS
                    led_strip[led_index] = sequence[j]

                led_strip.show()
                time.sleep(0.666)  # Timing based on 0.666 seconds

                # Exit the loop after going through once
                if i == NUM_LEDS - 1:
                    return

def create_led_pattern(led_strip):
                try:
                    while True:
                        led_strip.fill((0, 0, 0))  # Clear all LEDs

                        # Define the new color cues (Purple and Orange)
                        color_cues = [(128, 0, 128), (255, 165, 0)]  # Purple and Orange

                        for color in color_cues:
                            led_strip.fill(color)
                            led_strip.show()
                            time.sleep(0.333)  # Timing based on 0.333 seconds

def chaser_pattern(led_strip):
    led_strip.show()
        time.sleep(chase_speed)

        def chaser_pattern(led_strip):
            try:
                chase_color = (128, 0, 128)  # Purple color
                chaser_size = 5
                chase_speed = 0.111  # Adjust the speed of the chaser movement

                for i in range(len(led_strip)):
                    led_strip.fill((0, 0, 0))  # Clear all LEDs

                    for j in range(5):
                        led_index = (i + j) % len(led_strip)
                        led_strip[led_index] = chase_color

                    led_strip.show()
                    time.sleep(chase_speed)

        # Call the function to run the color sequence pattern in purple once
        color_sequence_pattern(led_strip)
        # Call the function to run the LED pattern with purple and orange colors
        create_led_pattern(led_strip)
        # Call the function to run the chaser pattern with purple color
        chaser_pattern(led_strip)
