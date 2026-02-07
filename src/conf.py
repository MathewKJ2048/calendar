import os
import json
import sys
from datetime import datetime
import time
import re

N = os.get_terminal_size().lines - 3

BLACK = "\033[30m"    # Dark gray or black
RED = "\033[31m"      # Dark red
GREEN = "\033[32m"    # Dark green
YELLOW = "\033[33m"   # Dark yellow/brown
BLUE = "\033[34m"     # Dark blue
MAGENTA = "\033[35m"  # Dark magenta
CYAN = "\033[36m"     # Dark cyan
WHITE = "\033[37m"    # Light gray



CLOSE = "\033[0m"

TAGS = {
	"none":WHITE,
	"work-event":BLUE,
	"deadline":RED,
	"life-event":GREEN,
}

DAYS = [
	"MON",
	"TUE",
	'WED',
	"THU",
	"FRI",
	RED+"SAT"+CLOSE,
	RED+"SUN"+CLOSE
	]

IDEAL_DAY_STRINGS = [
	"MONDAY",
	"TUESDAY",
	"WEDNESDAY",
	"THURSDAY",
	"FRIDAY",
	"SATURDAY",
	"SUNDAY"
]
