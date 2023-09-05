import board
import neopixel
import time

# LED SETUP
NUM_LEDS = 1  # You can adjust this for multiple LEDs
BRIGHTNESS_MIN = 0.1
BRIGHTNESS_MAX = 1.0
BREATHING_SPEED = 0.05  # Adjust the speed of the breathing effect

led_strip = neopixel.NeoPixel(board.D18, NUM_LEDS, brightness=BRIGHTNESS_MIN, auto_write=True)

def human_breathing_effect(led_strip):
    while True:
        # Simulate inhaling phase
        for brightness in range(int(BRIGHTNESS_MIN * 255), int(BRIGHTNESS_MAX * 255)):
            led_strip.brightness = brightness / 255.0
            time.sleep(BREATHING_SPEED)

        # Simulate exhaling phase
        for brightness in range(int(BRIGHTNESS_MAX * 255), int(BRIGHTNESS_MIN * 255), -1):
            led_strip.brightness = brightness / 255.0
            time.sleep(BREATHING_SPEED)

# Call the function to run the breathing effect
human_breathing_effect(led_strip)
