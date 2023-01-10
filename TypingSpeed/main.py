import curses

# We are going to use curses and more specifically the wrapper to help us
# overtake the terminal and be able to manipulate it. 
from curses import wrapper

import time
import random

def start_screen(stdscr):
    # Clear Screen
    stdscr.clear()
    # Print text. When providing a numbers before we indicate where to start
    # The first digit is for the line (1 line down) and the second is for the position
    # This allows you to print the second text before the first. Ex: "stdscr.addstr(1, 5, "Text2")"
    stdscr.addstr("Welcome to the Speed Typing Test!\n")
    stdscr.addstr("Press any key to begin:\n")

    # Refresh Screen
    stdscr.refresh()
    # Get in to waiting mode (for user input).
    # Important this helps us avoid the imediate closer of the scree/window
    key = stdscr.getkey()

# Display what user wrote
def display_text(stdscr, target, current_text, wpm = 0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")
    
    # Try to ilustrate the pros of using "enumerate". It basically gives us the char position in the
    # "current_text" list.
    for i, char in enumerate(current_text):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

# Load texts for a file and randomly display them
def load_text():
    # With context manager makes sure the file will be closed after we read it. Get of list
    # of the lines. With the "strip" method we remove the EOF charecter (any white space carecter actually).
    with open("texts.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

# Define Words Per Minute Test
def wpm_test(stdscr):

    target_text = load_text() 

    # Create a list of charecters to be printed on top of the original text
    current_text =  []

    wpm = 0
    start_time = time.time()

    # Do not delay waiting for the use key
    stdscr.nodelay(True)

    # In the while loop we add the key pressed to the current_text variable.
    # Then for loop we go through each char and print it out in different color 
    while True:
        # Calculate the time 
        time_elapsed = max(time.time() - start_time, 1)

        # WPM Equation (char per min). Assuming the average word has 5 letter we devide the WPM by 5
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
 
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        # Combine the elements of the list into a string with the delimiter ""
        # We want to give time to the user to hit a key and therefor we do the False nodelay
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        # Get the key pressed and protect again the user not typing anything by skipping the last
        # part of the function 
        try:
            key = stdscr.getkey()
        except:
            continue

        # Check if user hit "ESC" in order to quit the program
        if ord(key) == 27:
            break
        
        # Special keys setup. In different OS the backspace is represented by different char
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

        stdscr.clear()
        stdscr.addstr(target_text)


        # display_text(stdscr, target_text, current_text, wmp = 0):
 
def main(stdscr):
    # Colors pairs initiated, the first argument is the pair ID.
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(stdscr)

    while True:
        wpm_test(stdscr)
    
        stdscr.addstr(2, 0, "You completed the text! Press any key to play again")
        stdscr.getkey()
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break        
wrapper(main)

