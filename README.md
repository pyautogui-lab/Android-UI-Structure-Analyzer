# Android UI Structure Analyzer

🇯🇵 Japanese Documentation: [README_JP.md](README_JP.md)

A Python-based project for analyzing Android-style UI XML structures and extracting UI element information.
## Overview

This tool searches UI elements by resource-id, extracts bounds information, and calculates center coordinates from XML layout data.

## Features

* XML layout analysis
* UI element search by resource-id
* Bounds extraction
* Center coordinate calculation
## Technologies Used

* Python 3
* Regular Expressions (re)
* Dataclasses
* XML Parsing

## How to Run

1. Clone this repository.
2. Make sure `sample_window_dump.xml` is in the same directory as `ui_analyzer.py`.
3. Run the script:

```bash
python ui_analyzer.py
```

## Example Output

[1] resource-id: sample.app:id/target_button
    bounds: (120, 450) - (300, 520)
    center: (210, 485)

[2] resource-id: sample.app:id/target_button
    bounds: (400, 800) - (580, 870)
    center: (490, 835)
