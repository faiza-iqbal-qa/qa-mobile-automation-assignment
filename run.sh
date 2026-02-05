#!/usr/bin/env bash
set -e

source .venv/bin/activate

# Pick the first connected emulator/device if ANDROID_UDID not set
if [ -z "$ANDROID_UDID" ]; then
  export ANDROID_UDID="$(adb devices | awk 'NR==2{print $1}')"
fi

echo "Using ANDROID_UDID=$ANDROID_UDID"

# Appium should already be running. If not, start it.
if ! lsof -i :4723 >/dev/null 2>&1; then
  echo "Starting Appium..."
  appium > logs/appium_server.log 2>&1 &
  sleep 2
fi

python run_tests.py
