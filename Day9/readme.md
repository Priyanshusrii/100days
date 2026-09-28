## Overview
A command-line countdown timer that takes a duration from the user and counts down in real time, displaying the remaining time in a clean MM:SS format until the timer reaches zero.

## Features
- Set a custom duration in minutes and seconds
- Live-updating countdown displayed on a single line
- Alert message when the timer finishes
- Input validation for duration values
- Graceful handling of manual interruption

## Concepts Used
- Python `time` module
- Loops and functions
- String formatting and `divmod()`
- Exception handling (`KeyboardInterrupt`)

## Sample Usage
```
Enter min: 0
enter sec: 5

press ctrl+c to stop timer
00:05
00:04
00:03
00:02
00:01
time stopped
```