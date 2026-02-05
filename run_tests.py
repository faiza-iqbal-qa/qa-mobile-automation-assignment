import os
import subprocess
import sys

def main():
    os.makedirs("logs", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)

    cmd = [
        sys.executable, "-m", "pytest",
        "-q",
        "--disable-warnings",
        "--html=logs/report.html",
        "--self-contained-html"
    ]
    raise SystemExit(subprocess.call(cmd))

if __name__ == "__main__":
    main()
