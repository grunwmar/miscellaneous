from guard import Guard
import os

Guard.JSON_FILENAME = "data.json"
Guard.EXIT_AFTER_RUN = True

@Guard.run
def main(*args):
	for i in args:
		print(i)
	return 0



