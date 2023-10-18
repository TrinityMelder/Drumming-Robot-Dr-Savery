import board
import neopixel
import time
import random

# LED SETUP
NUM_LEDS = 96
BRIGHTNESS = 0.5
CHASE_SIZE = 5

# Use the appropriate pin
led_strip = neopixel.NeoPixel(board.Data, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)  

def three_color_sequence_pattern(): #Function 1
    
  for i in range(NUM_LEDS):
                red = (255, 0, 0)
                green = (0, 255, 0)
                blue = (0, 0, 255)

                if i % 3 == 0:
                    led_strip[i] = red
                    led_strip[i + 1] = green
                    led_strip[i + 2] = blue
                elif i % 3 == 1:
                    led_strip[i] = green
                    led_strip[i + 1] = blue
                    led_strip[i + 2] = red
                else:
                    led_strip[i] = blue
                    led_strip[i + 1] = red
                    led_strip[i + 2] = green

            # Show the pattern on the LED strip
            led_strip.show()

def random_color_pattern(): #Function 2
   
for i in range(NUM_LEDS): 
                # Generate a random color
                random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                # Set the current LED to the random color
                led_strip[i] = random_color

            # Show the pattern on the LED strip
            led_strip.show()

            # Delay before generating the next pattern
            time.sleep(1)     

def rainbow_colors_pattern(): #Function 3
   # Create a list of rainbow colors
            rainbow_colors = [
                (148, 0, 211),  # Violet
                (75, 0, 130),   # Indigo
                (0, 0, 255),    # Blue
                (0, 255, 0),    # Green
                (255, 255, 0),  # Yellow
                (255, 127, 0),  # Orange
                (255, 0, 0)     # Red
            ]
            
            # Display the rainbow colors on the LED strip
            for color in rainbow_colors:
                for i in range(NUM_LEDS):
                    led_strip[i] = color
                led_strip.show()
                time.sleep(1)  # Adjust the delay as desired
            
            # Turn off the LEDs before the next pattern
            led_strip.fill((0, 0, 0))
            led_strip.show()
            time.sleep(1)

def single_led_red_pattern(): #Function 4
    for i in range(NUM_LEDS):
            # Turn on the current LED in red
            led_strip.fill((0, 0, 0))  # Turn off all LEDs
            led_strip[i] = (255, 0, 0)  # Red
            led_strip.show()
            time.sleep(1)  # LED on time
            
            # Turn off the current LED
            led_strip[i] = (0, 0, 0)  # Turn off the current LED
            led_strip.show()
            time.sleep(1)  # Delay between LEDs

def chaser_pattern(): #Function 5
   for i in range(NUM_LEDS):
                led_strip.fill((0, 0, 0))  # Clear all LEDs

                for j in range(CHASE_SIZE):
                    led_index = (i + j) % NUM_LEDS
                    led_strip[led_index] = (0, 255, 0)  # Green color

                led_strip.show()
                time.sleep(1)  # Adjust the speed of the chaser movement

# Call the function to run the color sequence pattern
three_color_sequence_pattern()
random_color_pattern()
rainbow_colors_pattern()
single_led_red_pattern()
chaser_pattern()
