from conf import *

def validate_time(input_string):
	if len(input_string)!=4:
		return False
	for ch in input_string:
		if not ch.isdigit():
			return False
	det = int(input_string)
	return det%100<60 and det<2400

def get_current_epoch():
	return int(time.time())

def auxiliary_normalizer(input_string):
	if len(input_string)==1:
		return "0"+input_string
	return input_string

def to_epoch(date, time="0000"): # date in "YYYY-MM-DD"
	date = date.split("-")
	return int(datetime(int(date[0]),int(date[1]),int(date[2]),int
	(time[0]+time[1]),int(time[2]+time[3])).timestamp())

def to_date_time(epoch):
	strtime = datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H%M %S').split(" ")
	return strtime[0], strtime[1]

def day_of_week(epoch):
	return datetime.fromtimestamp(epoch).weekday()

def find_date_time(input_string):
	components = re.findall(r"\d+",input_string)
	components = [auxiliary_normalizer(c) for c in components]
	date_now, time_now = to_date_time(get_current_epoch())
	date_now = date_now.split("-")
	if len(components) == 1:
		return date_now[0]+"-"+date_now[1]+"-"+components[0]
	elif len(components) == 2:
		return date_now[0]+"-"+components[0]+"-"+components[1]
	elif len(components) == 3:
		return components[0]+"-"+components[1]+"-"+components[2]
	return date_now

def day_index(day):
	for i in range(len(IDEAL_DAY_STRINGS)):
		if IDEAL_DAY_STRINGS[i] == day:
			return i
	for i in range(len(DAYS)):
		if DAYS[i] == day:
			return i
	return -1

def color(tag_key,text):
	return TAGS[tag_key]+text+CLOSE