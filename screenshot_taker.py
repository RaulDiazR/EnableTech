import pyautogui
import time

# Set the interval between screenshots (in seconds)
interval = 0.65

# Set the total number of screenshots to capture
num_screenshots = 5

# Capture screenshots periodically
while True:
    for i in range(num_screenshots):
        # Generate a unique filename for each screenshot
        filename = f"screenshot_{i}.png"

        # Capture the screenshot
        screenshot = pyautogui.screenshot()

        # Save the screenshot
        screenshot.save(filename)

        # Print a confirmation message
        print(f"Screenshot saved: {filename}")

        # Wait for the specified interval
        time.sleep(interval)

