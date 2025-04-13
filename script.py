import pyautogui
import keyboard
import time
import os
import sys

pyautogui.PAUSE = 0.05
stop = False

def stop_on_keypress():
    global stop
    if keyboard.is_pressed('q'):
        print("Stopping...")
        stop = True

def confirm():
    stop_on_keypress()
    pyautogui.keyDown('z')
    pyautogui.keyUp('z')

def cancel():
    stop_on_keypress()
    pyautogui.keyDown('x')
    pyautogui.keyUp('x')


def up():
    stop_on_keypress()
    pyautogui.press('up')

def down():
    stop_on_keypress()
    pyautogui.press('down')



def open_buy_menu():
    confirm()
    down()


def use_8_times():
    for i in range(8):
        confirm()
        confirm()

# ---

def open_window(x, y):
    pyautogui.moveTo(x,y) 
    pyautogui.click()  


def buy_sequence():
    open_buy_menu()
    use_8_times()
    cancel()

def sell_sequence():
    down()
    confirm()
    use_8_times()
    up()


def show_status(coins, iters, i=0, iteration_time=None):
    os.system('cls')
    print(f"Farming {coins} coins in {iters} iterations.")
    print("Press 'q' to stop the script.")
    print()
    
    percentage = int((i / iters) * 100)
    print('#' * percentage + '-' * (100 - percentage) + f" {percentage:.2f}%")
    print(f"Completed {i}/{iters} iterations.")
    if iteration_time:
        print(f"{iteration_time*(iters-i):.2f} seconds remaining.")
    else:
        print("Estimating time remaining...")

def main():
    # screenWidth, screenHeight = pyautogui.size()
    # currentMouseX, currentMouseY = pyautogui.position()
    open_window(1483, 1064) 

    COINS_TO_GET = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    iters = int(COINS_TO_GET / 8)
    show_status(COINS_TO_GET, iters)

    for i in range(iters):
        iteration_time_start = time.time()
        buy_sequence()
        sell_sequence()
        if stop:
            print("Stopped by user.")
            break
        iteration_time_end = time.time()
        iteration_time = iteration_time_end - iteration_time_start
        show_status(COINS_TO_GET, iters, i+1, iteration_time)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()

    print()
    print("Farming completed!")
    print(f"--- %.2fs seconds ---" % (end_time - start_time))

