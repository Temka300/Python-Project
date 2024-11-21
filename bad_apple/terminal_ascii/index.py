import time

# Path to the text file containing all frames
file_path = "C:/Users/Temka/Desktop/Fubuzilla/Project/Python/Project/Hatsune Miku/miku_ascii.txt"

# Frame rate (frames per second)
fps = 12.0
frame_duration = 1.0 / fps

# Delimiter used to separate frames
delimiter = 'SPLIT'

def extract_frames(file_path, delimiter):
    frames = []
    with open(file_path, 'r') as file:
        content = file.read()
        frames = content.split(delimiter)
    # Remove empty frames if any
    frames = [frame.strip() for frame in frames if frame.strip()]
    return frames

def display_frame(frame_data):
    print(frame_data)

# Extract frames from the file
frames = extract_frames(file_path, delimiter)

# Loop through frames and display them
try:
    while True:
        for frame in frames:
            print("\033c", end="")  # ANSI escape code to clear the screen
            display_frame(frame)
            time.sleep(frame_duration)
except KeyboardInterrupt:
    print("\nAnimation stopped.")
