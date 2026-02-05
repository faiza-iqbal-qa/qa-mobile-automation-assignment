import os
import subprocess
import pytest
from datetime import datetime
from drivers.driver_factory import create_driver
from utils.logger import get_logger

log = get_logger()

APP_PACKAGE = "io.appium.android.apis"

def get_udid():
    udid = os.getenv("ANDROID_UDID")
    if udid:
        return udid
    # fallback first device
    out = subprocess.check_output(["adb", "devices"]).decode().strip().splitlines()
    if len(out) >= 2:
        return out[1].split()[0]
    return ""

def adb_cmd(args):
    udid = get_udid()
    base = ["adb"]
    if udid:
        base += ["-s", udid]
    cmd = base + args
    return subprocess.run(cmd, capture_output=True, text=True)

def clean_app_state():
    # force-stop and clear app data so it always starts from home list
    adb_cmd(["shell", "am", "force-stop", APP_PACKAGE])
    adb_cmd(["shell", "pm", "clear", APP_PACKAGE])
    log.info("Cleared API Demos app state (force-stop + clear)")

@pytest.fixture
def driver():
    clean_app_state()
    d = create_driver()
    yield d
    d.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        d = item.funcargs.get("driver")
        if not d:
            return

        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        shots_dir = os.path.join(root, "screenshots")
        os.makedirs(shots_dir, exist_ok=True)

        path = os.path.join(shots_dir, f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        try:
            d.save_screenshot(path)
            log.info(f"Saved screenshot on failure: {path}")
        except Exception as e:
            log.info(f"Could not save screenshot: {e}")
