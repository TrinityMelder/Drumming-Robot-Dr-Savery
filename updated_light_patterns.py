import board
import neopixel
import time
import random

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5


def color_sequence_pattern(led_strip):
    # change colours and just go through once (making timing based on 0.666)
    sequence = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # RGB color sequence
    for i in range(NUM_LEDS):
        led_colors = [sequence[i % 3], sequence[(i + 1) % 3], sequence[(i + 2) % 3]]

        for j in range(3):
            led_strip[i + j] = led_colors[j]
        led_strip.show()


def create_led_pattern(led_strip):
    # change the colors to match robot, and fix the bug

    color_cues = [(0, 255, 0), (0, 0, 255), (255, 0, 0)]  # Green, Blue, Red
    for _ in range(3):
        for color in color_cues:
            # Show the current color cue on all LEDs for the specified duration
            led_strip.fill(color)
            led_strip.show()
            time.sleep(0.333)


def chaser_pattern(led_strip):
    # more worms?
    chase_color = (8, 0, 21)  # Green color
    chaser_size = 5
    chase_speed = 0.111  # Adjust the speed of the chaser movement

    for i in range(len(led_strip)):
        led_strip.fill((0, 0, 0))  # Clear all LEDs

        for j in range(5):
            led_index = (i + j) % len(led_strip)
            led_strip[led_index] = chase_color

        led_strip.show()
        time.sleep(chase_speed)

def idle_pattern(led_strip):
    # Soft breathing effect with a calm blue color
    idle_color = (0, 0, 255)  # Soft blue
    for i in range(0, 255, 5):
        brightness = i / 255
        led_strip.fill((int(idle_color[0] * brightness), int(idle_color[1] * brightness), int(idle_color[2] * brightness)))
        led_strip.show()
        time.sleep(0.05)
    for i in range(255, 0, -5):
        brightness = i / 255
        led_strip.fill((int(idle_color[0] * brightness), int(idle_color[1] * brightness), int(idle_color[2] * brightness)))
        led_strip.show()
        time.sleep(0.05)

def rapping_pattern(led_strip):
    # Dynamic fast-changing pattern with vibrant colors
    rapping_colors = [(255, 0, 255), (255, 0, 0)]  # Purple and Red
    for _ in range(10):  # Repeat the pattern 10 times
        for color in rapping_colors:
            led_strip.fill(color)
            led_strip.show()
            time.sleep(0.1)  # Fast changes

def obstacle_detected_pattern(led_strip):
    # Flashing orange pattern to indicate obstacle detection
    obstacle_color = (255, 165, 0)  # Orange
    for _ in range(5):
        led_strip.fill(obstacle_color)
        led_strip.show()
        time.sleep(0.2)
        led_strip.fill((0, 0, 0))
        led_strip.show()
        time.sleep(0.2)

def thinking_pattern(led_strip):
    # Rotating yellow pattern to indicate thinking
    thinking_color = (255, 255, 0)  # Yellow
    for i in range(len(led_strip)):
        led_strip.fill((0, 0, 0))  # Clear all LEDs
        led_strip[i] = thinking_color
        led_strip.show()
        time.sleep(0.1)

def danger_alert_pattern(led_strip):
    # Intense flashing red pattern to indicate danger
    danger_color = (255, 0, 0)  # Red
    for _ in range(10):
        led_strip.fill(danger_color)
        led_strip.show()
        time.sleep(0.05)
        led_strip.fill((0, 0, 0))
        led_strip.show()
        time.sleep(0.05)
