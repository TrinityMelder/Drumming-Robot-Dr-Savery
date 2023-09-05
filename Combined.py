import board
import neopixel
import time
import random

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5

def color_sequence_pattern(led_strip, sequence, delay):
    try:
        while True:
            for i in range(NUM_LEDS):
                led_colors = [sequence[i % 3], sequence[(i + 1) % 3], sequence[(i + 2) % 3]]

                for j in range(3):
                    led_strip[i + j] = led_colors[j]

                # Show the pattern on the LED strip
                led_strip.show()

                # Delay before generating the next pattern
                time.sleep(delay)

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

def create_led_pattern(led_strip, color_cues, repetitions, cue_duration, inter_repetition_pause):
    try:
        while True:
            # Loop through each repetition of the pattern
            for _ in range(repetitions):
                for color in color_cues:
                    # Show the current color cue on all LEDs for the specified duration
                    led_strip.fill(color)
                    led_strip.show()
                    time.sleep(cue_duration)

                # Pause for the specified time between cues
                time.sleep(inter_repetition_pause)

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

def chaser_pattern(led_strip, chase_color, chase_size, chase_speed):
    try:
        while True:
            for i in range(len(led_strip)):
                led_strip.fill((0, 0, 0))  # Clear all LEDs

                for j in range(chase_size):
                    led_index = (i + j) % len(led_strip)
                    led_strip[led_index] = chase_color

                led_strip.show()
                time.sleep(chase_speed)

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

def run_led_patterns():
    led_strip = neopixel.NeoPixel(board.DATA, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)

    # Define user-provided cues for different patterns
    sequence_cues = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # RGB color sequence
    sequence_delay = 1  # Delay in seconds before generating the next pattern

    color_cues = [(0, 255, 0), (0, 0, 255), (255, 0, 0)]  # Green, Blue, Red
    color_repetitions = 3
    color_cue_duration = 0.2  # Duration for each color cue in seconds
    color_inter_repetition_pause = 1  # Pause between repetitions in seconds

    chaser_color = (0, 255, 0)  # Green color
    chaser_size = 5
    chaser_speed = 0.05  # Adjust the speed of the chaser movement

    try:
        while True:
            # Run each LED pattern function with its corresponding cues
            color_sequence_pattern(led_strip, sequence_cues, sequence_delay)
            create_led_pattern(led_strip, color_cues, color_repetitions, color_cue_duration, color_inter_repetition_pause)
            chaser_pattern(led_strip, chaser_color, chaser_size, chaser_speed)

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, turn off all LEDs and exit the program
        led_strip.fill((0, 0, 0))
        led_strip.show()

# Call the master function to run LED patterns
run_led_patterns()
