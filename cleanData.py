"""Outputs statistics for contact information FB has collected on you.

:author Ronad Rounsifer
:version 3/25/2018 (0.01)

Variables:
	__URL {str} -- url to users FB data page
	opened_url {urllib.response} -- opened data page
	soup {bs4.BeautifulSoup} -- bs4 object of data page
	divs {list} -- all of the divs in the pages HTML
	data_map {dict} -- contains parsed data
	num_contacts {int} -- number of contacts
	num_calls {int} -- number of phone calls
	num_texts {int} -- number of texts
	num_mms {int} -- number of multimedia messages
"""
from bs4 import BeautifulSoup
import urllib.request

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

num_contacts  = len(data_map["contacts"])#len(tables[0].find_all("tr"))
num_calls = len(data_map["call history"])
num_texts = len(data_map["sms history"])
num_mms = len(data_map["mms history"])

print("\n===== Facebook Data Analysis Script =====")
print("Number of contacts saved: %s" % (num_contacts))
print("Total number of phone calls: %s" % (num_calls))
print("Total number of text conversations: %s" % (num_texts))
print("Total number of multimedia conversations: %s" % (num_mms))
print("\n")