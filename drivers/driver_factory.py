import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

APP_PACKAGE = "io.appium.android.apis"

def create_driver():
    server_url = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
    udid = os.getenv("ANDROID_UDID", "")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android Emulator"
    if udid:
        options.udid = udid

    options.no_reset = False
    options.full_reset = False
    options.new_command_timeout = 300

    # BIG TIMEOUTS (fixes adb install timeout)
    options.set_capability("adbExecTimeout", 300000)  # 5 min for adb commands
    options.set_capability("uiautomator2ServerInstallTimeout", 600000)  # 10 min install
    options.set_capability("uiautomator2ServerLaunchTimeout", 600000)   # 10 min launch

    # Avoid incremental install edge cases
    options.set_capability("disableIdLocatorAutocompletion", True)

    driver = webdriver.Remote(server_url, options=options)
    driver.implicitly_wait(0)

    # bring API Demos to foreground
    try:
        driver.terminate_app(APP_PACKAGE)
    except Exception:
        pass
    driver.activate_app(APP_PACKAGE)

    return driver
