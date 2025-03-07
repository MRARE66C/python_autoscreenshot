import pyautogui
import datetime
import time
import random
import threading
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageEnhance
import json

SETTINGS_FILE = "settings.json"

def save_settings():
    settings = {
        "save_location": save_location,
        "min_interval": min_interval_entry.get(),
        "max_interval": max_interval_entry.get()
    }
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file)

def load_settings():
    global save_location
    try:
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)
            save_location = settings.get("save_location", "")
            min_interval_entry.insert(0, settings.get("min_interval", "10"))
            max_interval_entry.insert(0, settings.get("max_interval", "60"))
            if save_location:
                save_label.config(text=f"Save Location: {save_location}")
    except FileNotFoundError:
        pass

def enhance_image(image):
    # Convert to RGB mode if not already
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Apply more balanced enhancements
    image = ImageEnhance.Sharpness(image).enhance(1.5)    # Reduced sharpness to prevent artifacts
    image = ImageEnhance.Contrast(image).enhance(1.3)     # Increased contrast for better definition
    image = ImageEnhance.Color(image).enhance(1.2)        # Boost color saturation
    image = ImageEnhance.Brightness(image).enhance(1.15)   # Slightly increased brightness
    return image

def take_screenshot():
    if not save_location:
        messagebox.showerror("Error", "Please select a save location first!")
        return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{save_location}/screenshot_{timestamp}.jpg"  # Save as JPG
    screenshot = pyautogui.screenshot()
    
    # Enhance the image
    screenshot = enhance_image(screenshot)
    
    # Save as high-quality JPEG with maximum quality
    screenshot.save(filename, "JPEG", quality=100, optimize=True)
    print(f"Screenshot saved as {filename}")

def screenshot_loop():
    global running
    try:
        min_interval = int(min_interval_entry.get())
        max_interval = int(max_interval_entry.get())
        if min_interval <= 0 or max_interval <= 0 or min_interval > max_interval:
            messagebox.showerror("Error", "Please enter valid min and max interval values!")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for min and max interval!")
        return
    
    while running:
        wait_time = random.randint(min_interval, max_interval)
        time.sleep(wait_time)
        if running:
            take_screenshot()

def toggle_screenshots():
    global running, toggle_button
    if running:
        running = False
        toggle_button.config(text="Start")
        messagebox.showinfo("Info", "Screenshot capture stopped!")
    else:
        running = True
        thread = threading.Thread(target=screenshot_loop, daemon=True)
        thread.start()
        toggle_button.config(text="Stop")
        messagebox.showinfo("Info", "Screenshot capture started!")

def choose_save_location():
    global save_location
    save_location = filedialog.askdirectory()
    if save_location:
        save_label.config(text=f"Save Location: {save_location}")
        save_settings()

def exit_program():
    global running
    running = False
    save_settings()
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Screenshot Capturer")
root.geometry("400x400")  # Increased height to accommodate new button

running = False
save_location = ""

# Save location section
save_frame = tk.Frame(root)
save_frame.pack(pady=10)
tk.Button(save_frame, text="Choose Save Location", command=choose_save_location, width=25).pack()
save_label = tk.Label(save_frame, text="Save Location: Not selected", wraplength=380)
save_label.pack(pady=5)

# Interval settings section
interval_frame = tk.Frame(root)
interval_frame.pack(pady=10)
tk.Label(interval_frame, text="Min Interval (seconds):").pack()
min_interval_entry = tk.Entry(interval_frame, width=10)
min_interval_entry.pack(pady=2)
tk.Label(interval_frame, text="Max Interval (seconds):").pack()
max_interval_entry = tk.Entry(interval_frame, width=10)
max_interval_entry.pack(pady=2)

# Screenshot buttons section
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)
tk.Button(buttons_frame, text="Take Single Screenshot", command=take_screenshot, width=25).pack(pady=5)
toggle_button = tk.Button(buttons_frame, text="Start Auto Screenshots", command=toggle_screenshots, width=25)
toggle_button.pack(pady=5)

# Exit button
tk.Button(root, text="Exit", command=exit_program, width=25).pack(pady=10)

load_settings()
root.mainloop()

