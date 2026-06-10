# Android UI Structure Analyzer

🇯🇵 Japanese documentation: [README_JP.md](README_JP.md)

A Python-based proof-of-concept (PoC) project designed to analyze Android-style UI XML structures and dynamically extract UI element coordinates.

## Overview

This tool searches for target UI elements using their `resource-id`, extracts their `bounds` (coordinate boundaries), and calculates their exact geometric center. 
Furthermore, applying insights from wellness and cognitive research (the relationship between sleep quality and well-being), it incorporates a unique "human-like coordinate ripple" algorithm (`human_tap_point`) to simulate natural, non-mechanical tap positions.

The project was developed to deepen understanding of Android UI layouts and explore the integration of ergonomics and cognitive characteristics into UI automation.

## Features

* **High-Speed XML Parsing:** Robust pattern matching to parse complex UI layouts using regular expressions.
* **Target UI Element Discovery:** Automated filtering of UI nodes using specific `resource-id` attributes.
* **Boundary Information Extraction:** Reliable capturing of coordinate areas (`bounds`).
* **Geometric Center Calculation:** Precision arithmetic to determine absolute center points.
* **Human-Like Click Simulation:** Dynamic generation of subtle coordinate variations (ripples) restricted within safe button boundaries to avoid detectable rigid tap patterns.

## Tech Stack

* Python 3
* Regular Expressions (`re` module)
* Object-Oriented Data Structures (`dataclasses`)
* Robust Error Handling / Fallback Mechanism

## Execution Example

When executed with the bundled `sample_window_dump.xml`, the tool calculates both the absolute mechanical center and the dynamically shifted human-like tap point:

```text
==================================================
UI XML Parsing & Human-Like Tap Simulation
==================================================
[1] resource-id: sample.app:id/target_button
    Bounds (Area)    : (100, 500) - (300, 600)
    Absolute Center  : (200, 550) [Mechanical Center]
    Human-like Point : (203, 546) [Ergonomic Ripple Coordinate]
    Generated Offset : dX: 3px, dY: -4px (Safe variation based on button size)
--------------------------------------------------

## How to Run

You can easily test the coordinate parsing and ripple generation with the following steps:

1. Clone this repository to your local machine.
2. Ensure `sample_window_dump.xml` is located in the same directory as `ui_analyzer.py` (included by default).
3. Execute the script using Python:
```bash
   python ui_analyzer.py

## Key Learnings & Achievements

* **Interdisciplinary Approach (Tech × Ergonomics)**
  Successfully translated the conceptual framework that "rigid, mechanical rhythms cause systemic anomalies and friction" into a concrete mathematical algorithm (`human_tap_point`). This demonstrated a capability to synthesize non-technical domain research (wellness and cognitive characteristics) with rigorous programming logic.
* **Advanced Structured Data Extraction**
  Mastered regex non-greedy matching (`.+?`) to extract nested attribute pairs (`resource-id` and `bounds`) from large-scale hierarchical XML strings, ensuring a fast and lightweight parsing pipeline.
* **Modern Architecture & Encapsulation**
  Utilized Python `@dataclass` for elegant state management and `@property` decorators to encapsulate coordinate manipulation, ensuring a highly readable, modular, and maintainable codebase.
* **Defensive Programming & Portability**
  Implemented a safe fallback mechanism that automatically handles missing file scenarios to prevent system crashes, proving a strong awareness of software reliability, edge-case handling, and user experience.
* **Logical Debugging & Problem Solving**
  Encountered a critical bug during early development where multi-line UI elements failed to match. By comprehensively analyzing the parsing pipeline, identified that the regex dot (`.`) character does not match newline breaks by default. Resolved this by integrating the `re.DOTALL` flag, deepening understanding of regular expression mechanics and structured debugging methodologies.

## Development Background

This repository represents a streamlined, open-source adaptation of an internal technical validation tool. 

The original prototype was designed to run natively on Android devices using the **Termux** environment and **UIAutomator**, establishing a real-time loop of dumping live UI layouts, calculating target coordinates, and dispatching physical touch inputs.

For this public release, to ensure immediate testability and eliminate complex environmental dependencies (such as active ADB setups), the architecture was decoupled and optimized to run entirely via the bundled `sample_window_dump.xml`. This setup allows any user with a standard Python environment to immediately observe the coordinate ripple algorithm in action.

