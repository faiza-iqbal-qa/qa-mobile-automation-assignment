# QA Mobile Automation Assignment (Android)

This repository contains my solution for the Mobile UI Automation assignment. It is a Python-based test automation framework using **Appium** and **Pytest**, designed to automate user flows within the `ApiDemos-debug.apk` application.

[cite_start]The goal was to build a clean, maintainable, and robust test suite that not only executes the required scenarios but also handles failure gracefully with automated screenshots and detailed logging[cite: 5, 6].

---

## My Approach & Architecture

I approached this assignment with a focus on scalability and readability. Rather than writing a linear script, I implemented the **Page Object Model (POM)** design pattern.

* **Why POM?** I wanted to separate the test logic (assertions/flows) from the UI details (locators/elements). This makes the code easier to read and means that if a UI element changes ID, I only have to update it in one place (the `pages` folder) rather than every single test file.
* **Robust Interactions:** Handling mobile gestures like **Long Press** required using W3C Actions rather than deprecated Appium methods. [cite_start]I encapsulated this logic in the page objects to keep the test files clean.
* **Observability:** I set up a `conftest.py` fixture to automatically capture screenshots whenever a test fails, storing them in the `screenshots/` directory. [cite_start]This is critical for debugging "flaky" UI tests[cite: 35].
* [cite_start]**Simulated Flows:** As requested, I treated the "Long Press" on the context menu as an "Add to Cart" action and the navigation to the Custom Title screen as a "Checkout" flow, ensuring the logs reflect this business logic[cite: 28, 30].

---

## Project Structure

[cite_start]I organized the project strictly according to the assignment requirements[cite: 14]:

```text
├── drivers/           # Appium driver setup & APK management
├── pages/             # Page Object classes (Locators & interaction logic)
├── tests/             # Actual test scripts (Pytest)
├── utils/             # Helper functions (Logging, Explicit Waits)
├── screenshots/       # Auto-saved images on test failure
├── logs/              # Execution logs & HTML reports
├── requirements.txt   # Python dependencies
├── pytest.ini         # Test runner configuration
└── run.sh             # Execution shell script
