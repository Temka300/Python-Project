import pyautogui as pe
import time
import datetime
import threading
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("About to start")
time.sleep(3)

# Function to press 'Esc' every 20 minutes
def press_esc_periodically():
    while True:
        pe.press('esc')
        print("Pressed 'Esc' key")
        time.sleep(60)  # Sleep for 20 minutes

# Start the periodic 'Esc' press in a separate thread
esc_thread = threading.Thread(target=press_esc_periodically, daemon=True)
esc_thread.start()

while True:

    loop1 = 0
    loop2 = 0
    loop3 = 0
    loop4 = 0

    time.sleep(2)

    game_over = False
    time.sleep(3)
    while not game_over:
        location1 = pe.locateOnScreen("1.png", region=(36, 0, 120, 730), confidence=0.7)
        if location1:
            x1, y1 = pe.center(location1)
            time.sleep(2)
            pe.moveTo(x1, y1, duration=1)
            pe.click(clicks=2)
            
            print('Inner loop 1 done \n', end=' ')
            x = datetime.datetime.now()
            print(x)
            time.sleep(5)
            pe.moveTo(1904, 1008, duration=1)
            pe.click(clicks=1)

            pe.moveTo(1746, 875, duration=1)
            game_over = True
        else:
            loop1 += 1
            print(f'Inner loop 1 try again {loop1} \n', end=' ')
            time.sleep(5)

            if loop1 == 2:
                break

    time.sleep(2)

    game_over = False
    time.sleep(5)
    while not game_over:
        location2 = pe.locateOnScreen("2.png", region=(728, 352, 724, 510), confidence=0.7)
        if location2:
            pe.moveTo(1904, 1058, duration=1)
            pe.click(clicks=1)
            print('Inner loop 2 done \n', end=' ')
            game_over = True
        else:
            loop2 += 1
            print(f'Inner loop 2 try again {loop2} \n', end=' ')
            time.sleep(2)

            if loop2 == 2:
                break

    game_over = False
    time.sleep(0.5)
    while not game_over:
        location3 = pe.locateOnScreen("2.png", region=(728, 352, 724, 510), confidence=0.7)
        if location3:
            x1, y1 = pe.center(location3)
            time.sleep(2)
            pe.moveTo(x1, y1, duration=1)
            pe.click()
            print('Inner loop 3 done \n', end=' ')
            game_over = True
        else:
            loop3 += 1
            print(f'Inner loop 3 try again {loop3} \n', end=' ')
            time.sleep(3)

            if loop3 == 2:
                break