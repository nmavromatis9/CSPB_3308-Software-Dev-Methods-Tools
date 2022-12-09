#
# This script was written by: Nicolas Mavromatis
# Date: 8/25/22
# Purpose: Combining previous .html data extractions into one script
#Note: Part 1 said create 'clues.txt'. Part 2 did not. So I assume I should make it. 

#check that the file in paramter 1 exists
#paramter 0 is this filename

if [ -f $1 ]; then
	grep "clue_text" $1 | sort > clues.txt 
	grep "clue_text" $1 | sort | grep "clue_J" | sort > clues_J.txt
	grep "clue_text" $1 | sort | grep "clue_DJ" | sort > clues_DJ.txt
	grep "clue_text" $1 | sort | grep "clue_FJ" | sort > clues_FJ.txt
	grep "category_name" $1 | sort > category.txt
	wc -l *.txt
else 
	echo "Invalid or Missing filename"
	echo -n "Usage: "
	echo "$0 <filename>"
	echo ""
fi
