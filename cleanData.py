"""
Outputs statistics for contact information FB has collected on you.

:author Ronad Rounsifer
:version 3/25/2018 (0.01)
"""
from bs4 import BeautifulSoup
import urllib.request
import re

# static url
# no need for dynamic URL at this time
__URL = "file:///Users/user/Desktop/html/contact_info.htm"

# open file and make the HTML easier to read
opened_url = urllib.request.urlopen(__URL)
soup = BeautifulSoup(opened_url, 'html.parser')

# Find all divs in the HTML
divs = soup.find_all("div")

# divs[0] = navigation menu div
# divs[1] = entire page div
# divs[2] = parent div of divs[3] CAN IGNORE
# divs[3] = call history
# divs[4] = parent div of divs[5] CAN IGNORE
# divs[5] = mms history
# divs[6] = footer

data_map = { "everything" : divs[1],
				# all contacts belong to the meta class
				"contacts" : divs[1].find_all(class_="meta"),
				"call history" : divs[3],
				"sms history" : divs[4],
				"mms history" : divs[5]
				}

# Overview of all the data data on the page
num_contacts  = len(data_map["contacts"])#len(tables[0].find_all("tr"))
num_calls = len(data_map["call history"])
num_texts = len(data_map["sms history"])
num_mms = len(data_map["mms history"])

table_data = []

for call_info in data_map["call history"].find_all('td'):
	table_data.append(call_info)


# specifics for recorded all histories
outgoing_calls = 0
rejected_calls = 0
missed_calls = 0
incoming_calls = 0
users_name = "Ronald Rounsifer" # TODO make this dynamic 

for x in table_data:
	if x.string == "OUTGOING":
		outgoing_calls += 1
	elif x.string == "REJECTED":
		rejected_calls += 1
	elif x.string == "MISSED":
		missed_calls += 1
	elif x.string == "INCOMING":
		incoming_calls += 1

total_time_minutes = 0

for call_info in table_data:
	# use regex to search for only numbers
	if (re.search('^[0-9]+$', str(call_info.string))):
		total_time_minutes += int(call_info.string)

def showData():
	print("\n===== Facebook Data Analysis Script =====")
	print("All of this data has been collected by facebook for the account of %s" % (users_name))
	print("Number of contacts saved: %s" % (num_contacts))
	print("Total number of phone calls: %s" % (num_calls))
	print("Total number of text conversations: %s" % (num_texts))
	print("Total number of multimedia conversations: %s" % (num_mms))
	print("\n")
	print("=== Phone call data ===")
	print("Outgoing: %s" % (outgoing_calls))
	print("Incoming: %s" % (incoming_calls))
	print("Rejected: %s" % (rejected_calls))
	print("Missed: %s" % (missed_calls))
	print("Time spent in calls: %s minutes" % (total_time_minutes//60))
	print("\n")

showData()