# This is a pretty bad code

from pynput.mouse import Listener
import pyautogui
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

positions = []
editor = None
pos1_label = None
pos2_label = None

# Function called when mouse is clicked
def on_click(x, y, button, pressed):
    if pressed:
        positions.append((x, y))
        print(f"Position captured: {x}, {y}")
        update_gui_positions(len(positions), x, y)

        if len(positions) == 2:
            take_screenshot(positions[0], positions[1])
            return False  # Stop the listener

# Function to take screenshot based on two positions
def take_screenshot(pos1, pos2):
    # Define the bounding box
    left = min(pos1[0], pos2[0])
    top = min(pos1[1], pos2[1])
    right = max(pos1[0], pos2[0])
    bottom = max(pos1[1], pos2[1])

    # Take screenshot using pyautogui
    screenshot = pyautogui.screenshot(region=(left, top, right - left, bottom - top))
    screenshot.save("captured_area.png")
    print("Screenshot saved as captured_area.png")

    # Open the GUI to display and crop the image
    open_image_editor("captured_area.png")

# Function to open the image editor GUI
def open_image_editor(image_path):
    global editor, pos1_label, pos2_label

    # Create a Tkinter window
    editor = tk.Tk()
    editor.title("Image Cropper")

    # Load the image
    img = Image.open(image_path)
    img_tk = ImageTk.PhotoImage(img)

    # Create a canvas to display the image
    canvas = tk.Canvas(editor, width=img.width, height=img.height)
    canvas.pack()
    canvas_img = canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

    # Variables to store crop coordinates
    crop_coords = [0, 0, img.width, img.height]

    # Function to handle mouse click events on the canvas
    def on_canvas_click(event):
        crop_coords[0] = event.x
        crop_coords[1] = event.y
        print(f"Crop start position: ({event.x}, {event.y})")

    # Function to handle mouse release events on the canvas
    def on_canvas_release(event):
        crop_coords[2] = event.x
        crop_coords[3] = event.y
        print(f"Crop end position: ({event.x}, {event.y})")

    # Bind mouse events to the canvas
    canvas.bind("<ButtonPress-1>", on_canvas_click)
    canvas.bind("<ButtonRelease-1>", on_canvas_release)

    # Function to save the cropped image
    def save_cropped_image():
        left = min(crop_coords[0], crop_coords[2])
        top = min(crop_coords[1], crop_coords[3])
        right = max(crop_coords[0], crop_coords[2])
        bottom = max(crop_coords[1], crop_coords[3])

        cropped_img = img.crop((left, top, right, bottom))
        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if save_path:
            cropped_img.save(save_path)
            print(f"Cropped image saved as {save_path}")

    # Save button
    save_button = tk.Button(editor, text="Save Cropped Image", command=save_cropped_image)
    save_button.pack()

    # Labels to show captured positions
    pos1_label = tk.Label(editor, text="Position 1: Not Captured")
    pos1_label.pack()
    pos2_label = tk.Label(editor, text="Position 2: Not Captured")
    pos2_label.pack()

    # Run the Tkinter event loop
    editor.mainloop()

# Function to update position labels
def update_gui_positions(pos_num, x, y):
    global pos1_label, pos2_label
    if pos1_label is not None and pos2_label is not None:
        if pos_num == 1:
            pos1_label.config(text=f"Position 1: ({x}, {y})")
        elif pos_num == 2:
            pos2_label.config(text=f"Position 2: ({x}, {y})")

# Start listening to mouse clicks
with Listener(on_click=on_click) as listener:
    listener.join()