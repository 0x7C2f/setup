#!/usr/bin/env bash

echo "Launching Polybar script at $(date)" >> /tmp/polybar_launch.log

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch Polybar on each monitor
if type "xrandr"; then
  for m in $(xrandr --listmonitors | grep ' ' | cut -d' ' -f6); do
    MONITOR=$m polybar --reload top &
  done
else
  polybar --reload top &
fi
