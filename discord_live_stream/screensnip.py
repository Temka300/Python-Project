import keyboard
import pyautogui
from PIL import ImageGrab
import time

def take_screenshot_between_coords(coord1, coord2):
    # Determine the top-left and bottom-right corners of the rectangle
    x1, y1 = coord1
    x2, y2 = coord2
    top_left_x = min(x1, x2)
    top_left_y = min(y1, y2)
    bottom_right_x = max(x1, x2)
    bottom_right_y = max(y1, y2)

    # Calculate the region width and height
    width = bottom_right_x - top_left_x
    height = bottom_right_y - top_left_y

    # Print the top-left coordinates and region dimensions
    print(f"Top-left coordinates: ({top_left_x}, {top_left_y})")
    print(f"Region width: {width}, Region height: {height}")

    # Ask the user for the screenshot file name
    file_name = input("Enter the name of the screenshot file (without .png): ") + ".png"

    # Take the screenshot
    screenshot = ImageGrab.grab(bbox=(top_left_x, top_left_y, bottom_right_x, bottom_right_y))
    screenshot.save(file_name)
    print(f"Screenshot saved as {file_name}")

def get_coordinates():
    print("Click on the first location...")
    x1, y1 = pyautogui.position()
    time.sleep(0.1)  # Small delay to ensure the position is captured correctly
    #pyautogui.click()  # Simulate the first click
    print(f"First coordinate Top-left: ({x1}, {y1})")

    print("Press Alt+Z again to capture the second location...")
    while True:
        if keyboard.is_pressed('alt+z'):
            time.sleep(0.5)  # Small delay to avoid double detection of the key press
            x2, y2 = pyautogui.position()
            #pyautogui.click()  # Simulate the second click
            print(f"Second coordinate Bottom-right: ({x2}, {y2})")
            return (x1, y1), (x2, y2)

def start_script():
    print("Script started. Press Alt+Z to run the program.")

    while True:
        if keyboard.is_pressed('alt+z'):
            print("Alt+Z detected. Waiting for mouse clicks...")
            coord1, coord2 = get_coordinates()
            take_screenshot_between_coords(coord1, coord2)
            break

        time.sleep(0.1)

if __name__ == "__main__":
    start_script()
