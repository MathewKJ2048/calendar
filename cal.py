from conf import *
import json
import sys
from datetime import datetime
import time
import re

INTERVAL = 24*60*60

filepath = sys.argv[1]
calendar = json.load(open(filepath))
times = []

def initialize(n):
	global calendar
	global times
	date, time = to_date_time(get_current_epoch())
	t0 = to_epoch(date)
	times = []
	for i in range(n):
		times.append(t0+i*INTERVAL)

def save():
	global filepath
	json.dump(calendar,open(filepath,"w"),indent=4)

def get_current_epoch():
	return int(time.time())

def to_epoch(date, time="0000"): # date in "YYYY-MM-DD"
	date = date.split("-")
	return int(datetime(int(date[0]),int(date[1]),int(date[2]),int
	(time[0]+time[1]),int(time[2]+time[3])).timestamp())

def to_date_time(epoch):
	strtime = datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H%M %S').split(" ")
	return strtime[0], strtime[1]

def day_of_week(epoch):
	return datetime.fromtimestamp(epoch).weekday()

def find_day(input_string):
	global times
	refined = ""
	for ch in input_string:
		if ch.isalpha():
			refined+=ch
	refined = refined.upper()
	for d in IDEAL_DAY_STRINGS:
		if refined in d:
			return d
	return IDEAL_DAY_STRINGS[day_of_week(get_current_epoch())]

def find_nearest_date(day):
	for t in times[1:]:
		if IDEAL_DAY_STRINGS[day_of_week(t)] == day:
			return to_date_time(t)[0]
	return to_date_time(times[0])[0]

def find_date_time(input_string):
	components = re.findall(r"\d+",input_string)
	date_now, time_now = to_date_time(get_current_epoch())
	date_now = date_now.split("-")
	if len(components) == 1:
		return date_now[0]+"-"+date_now[1]+"-"+components[0]
	elif len(components) == 2:
		return date_now[0]+"-"+components[0]+"-"+components[1]
	elif len(components) == 3:
		return components[0]+"-"+components[1]+"-"+components[2]
	return date_now


def find_universal(input_string):
	if any(ch.isdigit() for ch in input_string):
		return find_date_time(input_string)
	return find_nearest_date(find_day(input_string))

def display():
	def k(e):
		time = e["time"]
		if time == "0000":
			return "9"+time
		return time
	print("┏━━┳━━━┓")
	for t in times:
		date, time = to_date_time(t)
		print("┃"+date[-2]+date[-1]+"┃"+DAYS[day_of_week(t)]+"┃",end="")
		events = []
		for event in calendar["singular_events"]:
			if event["date"] == date:
				events.append(event)
		for event in calendar["weekly_events"]:
			if IDEAL_DAY_STRINGS[day_of_week(t)] == find_day(event["day"]):
				events.append(event)
		events.sort(key=k)
		for event in events:
			disp_string = ""
			if event["time"] != "0000":
				disp_string = "["+event["time"]+"]"+" "
			disp_string+=event["name"]
			print(TAGS[event["tag"]]+disp_string+CLOSE,end="┃")
		print("")
	print("┗━━┻━━━┛")

def validate_time(input_string):
	if len(input_string)!=4:
		return False
	for ch in input_string:
		if not ch.isdigit():
			return False
	det = int(input_string)
	return det%100<60 and det<2400

def add_event():
	event = input("event name:")
	date = find_universal(input("date:"))
	ti = str(input("time:"))
	if not validate_time(ti):
		ti = "0000"
	print("")
	tag_list = []
	for t in TAGS:
		tag_list.append(t)
	for i in range(len(tag_list)):
		print(str(i)+") "+tag_list[i])
	tag = tag_list[int(input("tag:"))]
	print("")

	print(TAGS[tag]+event+CLOSE+" at "+ti+" on "+date+" ("+IDEAL_DAY_STRINGS[day_of_week(to_epoch(date,ti))]+")")
	t = input("confirmation (y/n)")
	if t=='n' or t=='N':
		return
	event_entry = {
		"name":event,
		"time":ti,
		"date":date,
		"tag":tag
	}
	calendar["singular_events"].append(event_entry)
	save()
	print("event added")




if len(sys.argv) <= 2:
	initialize(N)
	display()
else:
	if sys.argv[2] == "add":
		add_event()
	else:
		initialize(int(sys.argv[2]))
		display()
