# QA Automation Engineer Assignment (Android) - Appium + Python

## Project Structure
- tests/        - pytest tests and fixtures
- drivers/      - Appium driver setup
- utils/        - waits and logging utilities
- screenshots/  - screenshots captured on failures
- logs/         - logs and HTML report

## Prerequisites
- Android Studio + Emulator
- Node.js
- Appium (server)
- Python 3

## Setup
1) Install Python deps:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2) Install Appium driver:
   appium driver install uiautomator2

3) Install API Demos app on emulator:
   adb install -r ApiDemos-debug.apk

## Run
Start emulator + Appium server, then run:
./run.sh

## Outputs
- logs/report.html
- logs/*.log
- screenshots/*.png (on test failures)

## Automated Scenario
1) Verify home screen loads by asserting "Views"
2) Navigate Views -> Expandable Lists -> 1. Custom Adapter
3) Long press "People Names" and assert "Sample menu" appears
4) Treat context menu appearance as confirmation and log it
5) Navigate back -> App -> Activity -> Custom Title
6) Assert "Left is best" and "Right is always right" are present
