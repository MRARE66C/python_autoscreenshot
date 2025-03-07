# Screenshot Capturer

A Python-based desktop application for taking high-quality screenshots with automatic enhancement features. The application supports both single screenshots and automated interval-based captures.

## Features

- 📸 Single screenshot capture
- 🔄 Automated screenshot capture with random intervals
- 🎨 Automatic image enhancement:
  - Sharpness optimization
  - Contrast improvement
  - Color saturation boost
  - Brightness adjustment
- 💾 High-quality JPEG output (100% quality)
- 📁 Customizable save location
- ⏱️ Configurable capture intervals
- 🔧 Settings persistence between sessions

## Requirements

- Python 3.6 or higher
- Required Python packages:
  ```
  pyautogui
  Pillow
  ```

## Installation

1. Clone or download this repository
2. Install the required packages:
   ```bash
   pip install pyautogui Pillow
   ```

## Usage

1. Run the application:
   ```bash
   python screenshot.py
   ```
   or double-click `start.bat` on Windows

2. Configure the application:
   - Click "Choose Save Location" to select where screenshots will be saved
   - Set minimum and maximum intervals (in seconds) for automated captures

3. Taking Screenshots:
   - Click "Take Single Screenshot" for an immediate capture
   - Click "Start Auto Screenshots" to begin automated captures
   - Click "Stop" to end automated capture session

## File Naming

Screenshots are automatically saved with timestamps in the format:
```
screenshot_YYYY-MM-DD_HH-MM-SS.jpg
```

## Image Enhancement

All screenshots are automatically enhanced with:
- Sharpness enhancement (1.5x)
- Contrast boost (1.3x)
- Color saturation increase (1.2x)
- Slight brightness improvement (1.15x)

## Settings

The application saves your preferences in `settings.json`, including:
- Last used save location
- Minimum interval time
- Maximum interval time

## Notes

- The application must have permission to access the screen for screenshots
- Screenshots are saved in high-quality JPEG format
- The random interval feature helps in capturing unpredictable moments

## License

This project is open source and available under the MIT License. 