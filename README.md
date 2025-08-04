# Temperature Scale GUI with Tkinter

This Python application uses the Tkinter library to simulate a vertical temperature scale with real-time feedback. The interface provides dynamic temperature readings, visual cues for extreme temperatures, and context-aware messages.

---

## Features

- Vertical temperature scale ranging from **100°C to 0°C**
- Real-time temperature display that updates as the user moves the slider
- Temperature value color changes based on range:
  - **Red** for hot temperatures (> 66°C)
  - **Orange** for moderate temperatures (34°C – 66°C)
  - **Blue** for cold temperatures (≤ 33°C)
- Submit button prints messages depending on the current temperature:
  - Alerts for freezing (0°C) and overheating (100°C) conditions
- Simple, portable UI using built-in text and labels

---

## Getting Started

### Requirements

- Python 3.x
- Tkinter (included with most Python installations)

### Running the Application

Save the file as `temperature_scale.py` and run it:

```bash
python temperature_scale.py
