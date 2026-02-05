

```markdown
# Mobile Automation Assignment (Android)
### Python + Pytest + Appium (Page Object Model)

A robust mobile automation framework for Android using the **Page Object Model (POM)** pattern. This project automates specific user journeys within the Android `ApiDemos-debug.apk` to demonstrate proficiency in element locators, gesture handling (long press), and automated reporting.

---

## 🏗 Project Structure

```text
├── drivers/           # Appium driver configurations & capabilities
├── pages/             # Page Object classes (UI elements & actions)
├── tests/             # Pytest test cases and conftest.py (fixtures)
├── utils/             # Explicit waits, logging, and common helpers
├── screenshots/       # Automatic screenshot capture on test failure
├── logs/              # Execution logs and HTML test reports
├── requirements.txt   # Python dependencies
├── pytest.ini         # Pytest configuration
└── run.sh             # Shell script to execute the suite

```

---

## 🚀 Key Features

* **Page Object Model (POM):** Separates test logic from UI locators for high maintainability.
* **Gestures:** Implementation of W3C Actions for complex interactions like **Long Press**.
* **Automatic Reporting:** Generates detailed HTML reports in the `logs/` directory.
* **Failure Handling:** Automatically captures screenshots when a test step fails.
* **Logging:** Comprehensive step-by-step logging for debugging execution flow.

---

## 🛠 Prerequisites

Ensure you have the following installed:

* **Java JDK 11+**
* **Android Studio** (with an Emulator configured)
* **Node.js & Appium Server** (`npm install -g appium`)
* **UiAutomator2 Driver** (`appium driver install uiautomator2`)
* **Python 3.10+**

---

## 💻 Setup & Execution

1. **Clone the repository:**
```bash
git clone [https://github.com/faiza-iqbal-qa/qa-mobile-automation-assignment.git](https://github.com/faiza-iqbal-qa/qa-mobile-automation-assignment.git)
cd qa-mobile-automation-assignment

```


2. **Setup Virtual Environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

```


3. **Install the App:**
Ensure your emulator is running, then install the target APK:
```bash
adb install drivers/ApiDemos-debug.apk

```


4. **Run Tests:**
Start the Appium server, then execute:
```bash
chmod +x run.sh
./run.sh

```



---

## 🧪 Automated Scenarios

### Scenario 1: Expandable Lists & Context Menus

* Navigates to **Views** > **Expandable Lists** > **1. Custom Adapter**.
* Performs a **Long Press** on "People Names".
* Asserts that the "Sample menu" context menu appears.

### Scenario 2: Custom Title Validation

* Navigates to **App** > **Activity** > **Custom Title**.
* Validates the presence of specific text views: "Left is best" and "Right is always right".

---

## 📊 Reporting

After execution, find the results here:

* **HTML Report:** `logs/report.html`
* **Execution Logs:** `logs/automation.log`
* **Screenshots:** Check `screenshots/` if any tests failed.

```

### Recommendation:
Since your project contains folders like `.pytest_cache`, you should update your `.gitignore` to prevent these temporary files from cluttering your repo. 

**Add this to your `.gitignore` file:**
```text
.pytest_cache/
__pycache__/
*.py[cod]
.venv/
logs/*.log
logs/*.html
screenshots/*.png
.DS_Store

```
