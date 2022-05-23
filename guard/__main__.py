from guard import Guard
import os

# Guard.JSON_FILENAME = "data.json"

@Guard.run
def main(*args):
	for i in args:
		print(i)


print(Guard.INFO)

