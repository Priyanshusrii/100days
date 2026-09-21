## Overview

A command-line Madlibs story generator that lets users choose a genre, enter a name, and generate a random story with a line-by-line time delay.

## Features

* Choose from 10 different story genres
* Enter a desired name for the story
* 3 different stories for each genre
* Randomly selects a story from the chosen genre
* Displays the story line by line with a 2-second delay
* Option to keep generating new stories

## Concepts Used

* Python `random` module
* Python `time` module
* `random.choice()`
* `while` loops and `match-case`
* Lists for storing stories
* F-strings for inserting user input
* String `splitlines()` for line-by-line output

## Sample Usage

```text
1:Horror👻   2:Sci-fi🚀   3:Mystery🔎   4:Fantasy🐉

Select genre: 1

Enter a desired name: rexy

At midnight, rexy entered the abandoned Blackwood Mansion.

A shadow slowly walked down the hallway toward rexy.

Every light suddenly went out, leaving only silence.

When the lights returned, rexy was no longer alone.
```
