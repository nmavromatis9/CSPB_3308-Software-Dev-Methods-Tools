import sys
import random

HEADER = '''
### User Story : %d
<hr>
'''

US_FORMAT = '* *%s*   %s'

TRAILER = '''
<hr>

Effort Estimation

* **Level:**<br><br>

<hr>

Acceptance Criteria

* **Given:** 	\<context of action\><br><br>
	
* **When :** 	\<some action is completed\><br><br>
	
* **Then :** 	\<set of observable outcomes\><br><br>
	
<hr><hr><br><br>
'''


def main (argc, argv) :

	
	
	if argc > 1 : 
		# get list of item numbers to include in the output
		items = [int(arg) for arg in argv[1:]]
	else:
		# Create a set of 5 for all output + set of 5 random from 0..14
		items = [1, 2, 3, 4, 5]  # counter is 1 based
		while (len(items) < 10) :
			item = random.randrange(5, 20)	+ 1  # counter is 1 based, assumes 20 user stories total
			if (item not in items) :
				items.append(item)  
		
		
	print ("### Stories included: ", items)
	
	with open('User_Stories.txt') as f:
		counter = 0
		for line in f:
			line = line.strip()
			if (len(line) == 0) : continue

			fields = [x.strip() for x in line.split('\t')]

			if (fields[0] == "As a") : 
				counter += 1
				if (counter in items) :
					print (HEADER%counter)
					print (US_FORMAT%(fields[0], fields[1]))

			if (fields[0] == "I want") : 
				if (counter in items) :
					print (US_FORMAT%(fields[0], fields[1]))

			if (fields[0] == "So that") : 
				if (counter in items) :
					print (US_FORMAT%(fields[0], fields[1]))
					print (TRAILER)

				
if __name__ == "__main__":
	main(len(sys.argv), sys.argv)
	
	