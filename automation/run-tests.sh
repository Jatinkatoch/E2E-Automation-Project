#!/bin/bash

set -e

mkdir -p videos screenshots traces reports

if [ "$HEADLESS" = "false" ]; then

    echo "Running headed mode"

    export DISPLAY=:99

    echo "Starting Xvfb..."

    Xvfb :99 -screen 0 1920x1080x24 -ac &
    
    sleep 5

    echo "Starting fluxbox..."

    fluxbox &

    sleep 2

    echo "Starting x11vnc..."

    x11vnc \
    -display :99 \
    -forever \
    -nopw \
    -listen 0.0.0.0 \
    -xkb &

    sleep 2

    echo "Starting noVNC..."

    websockify \
    --web=/usr/share/novnc \
    6080 \
    localhost:5900 &

    sleep 3

    echo "======================================"
    echo "View test execution live at:"
    echo "http://localhost:6080/vnc.html"
    echo "========================================"

else

    echo "Running headless mode"

fi

pytest "$@"