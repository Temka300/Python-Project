from pynput.mouse import Listener
import pyautogui
from PIL import Image

positions = []

def on_click(x, y, button, pressed):
    if pressed:
        positions.append((x, y))
        print(f"Position captured: {x}, {y}")
        
        if len(positions) == 2:
            take_screenshot(positions[0], positions[1])
            return False  # Stop the listener

def take_screenshot(pos1, pos2):
    # Define the bounding box
    left = min(pos1[0], pos2[0])
    top = min(pos1[1], pos2[1])
    right = max(pos1[0], pos2[0])
    bottom = max(pos1[1], pos2[1])
    
    # Take screenshot using pyautogui
    screenshot = pyautogui.screenshot(region=(left, top, right - left, bottom - top))
    
    # Save the screenshot
    screenshot.save("captured_area.png")
    print("Screenshot saved as captured_area.png")

# Start listening to mouse clicks
with Listener(on_click=on_click) as listener:
    listener.join()