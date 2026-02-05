# Mobile UI Automation Assignment

This repository contains my solution for the Android automation assignment. It is a Python-based framework using **Appium** and **Pytest**, designed to validate specific user flows within the `ApiDemos-debug.apk` application.

## Approach & Architecture

I prioritized creating a framework that is scalable rather than just writing a linear script. Here is how I handled the specific requirements:

* **Page Object Model (POM):** I separated the test logic (assertions) from the UI interactions (locators). This ensures that if a UI element changes, we only need to update the specific Page class, keeping the tests clean.
* **Modern Gestures:** The assignment required a "Long Press" interaction. Since the old `TouchAction` class is deprecated in Appium 2.0, I implemented this using W3C Actions to ensure future compatibility.
* **Simulated Business Logic:** Per the problem statement, I treated specific technical actions (like the Context Menu appearance) as simulated business events (e.g., "Item Added to Cart") in the logs to demonstrate how technical tests map to user value.
* **Resilience:** I added a `conftest.py` fixture to automatically capture screenshots immediately upon test failure, aiding in rapid debugging.

## Project Structure

The project follows the strict folder structure requested:

* `drivers/` - Contains the APK and driver configurations.
* `pages/` - Page Object classes where locators and methods live.
* `tests/` - The actual test scripts and fixtures.
* `utils/` - Helper methods for logging and explicit waits.
* `screenshots/` - Automatically stores images when a test fails.
* `logs/` - Execution logs and HTML reports.

## Prerequisites

* **Python 3.10+**
* **Appium Server** (running via Node.js)
* **Android SDK** (with Emulator configured)
* **Java JDK**

## Setup Instructions

1.  **Environment Setup**
    Create a virtual environment to keep dependencies clean:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

2.  **Install the Driver**
    Ensure the UiAutomator2 driver is installed for Appium:
    ```bash
    appium driver install uiautomator2
    ```

3.  **Install the App**
    Launch your Android Emulator and install the demo app:
    ```bash
    adb install drivers/ApiDemos-debug.apk
    ```

## Execution

I have included a shell script to simplify execution. This handles running the tests and generating the report.

**To run the full suite:**
```bash
chmod +x run.sh
./run.sh

```

**To run manually via Pytest:**

```bash
pytest tests/ --html=logs/report.html --self-contained-html

```

## Scenarios Covered

The test suite covers the following journey:

1. **Home Screen Validation**
* Launch app and verify the "Views" menu is visible.


2. **"Add to Cart" Simulation**
* Navigate: *Views -> Expandable Lists -> Custom Adapter*.
* Action: Perform a **Long Press** on "People Names".
* Verification: Assert "Sample menu" appears (Logged as: *Item added to cart*).


3. **"Checkout" Simulation**
* Navigate: *Back -> App -> Activity -> Custom Title*.
* Verification: specific text elements ("Left is best") are present to confirm the screen loaded (Logged as: *Checkout screen verified*).



## Outputs

* **Logs:** Check `logs/automation.log` for step-by-step execution details.
* **Reports:** Open `logs/report.html` for a visual summary.
* **Screenshots:** If a failure occurs, the screenshot will appear in `screenshots/`.

```

```
