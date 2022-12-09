#!/bin/bash
#
#  Need to recreate the following commit tree with three branches.
#  Each commit uses a different sample HTML file from this data directory.
#
# | *  "# 9.  updated the task instructions"  (TASKS)
# | *  "# 8.  added student tasks" 
# * |    merge DEV into MAIN 
# |\ \  
# | * |  "#11. added  3308 logo"  (DEV)
# | * |  "# 7. add CU logo " 
# | |/  
# | *  "# 6.  add text to be changed by student" 
# | *  "# 5. modified text specifically for 3308" 
# | *  "# 4. added text for page title" 
# * |  "#10. show a comment tag, capitalized words" 
# |/  
# *  "# 3. add the minimal HTML tags" 
# *  "# 2. update the text to use header tag" 
# *  # 1. simplest HTML page 
#

CP='cp'
GIT='git'
GIT_FIRST_BRANCH='master'
WAIT_TIME=10

# for debugging
# set -x #echo on
# CP='echo cp'
# GIT='echo git'
# echo "WAIT_TIME = [$WAIT_TIME]"
#echo "GIT_LOG = [$GIT_LOG]"

function make_commit { 
	$CP sample$1.html sample.html
	$GIT add sample.html 
	$GIT commit -m "\"$2\""

	if [ -n "$WAIT_TIME" ]; then
		$GIT log --graph  --format=format:'%C(yellow) %s %d' --all
		read -t $WAIT_TIME -n 1 -s -r -p "press any key to continue..." 
		echo ""
	fi
}

# 1. initial sample HTML file - (MAIN)  - file will be there from Classroom CLONE
#    change branch `main` (or `master`) to `MAIN` -  just so we know it is the demo we are manipulating

echo "hello world!" > sample.html
$GIT add sample.html 
$GIT commit -m "# 1. simplest HTML page"
$GIT branch -m $GIT_FIRST_BRANCH MAIN

if [ -n "$WAIT_TIME" ]; then
	read -t $WAIT_TIME -n 1 -s -r -p "Press any key to continue" 
	echo ""
fi

# Add a couple more commits to the MAIN branch
make_commit 2 "# 2. updated the text to use header tag"

make_commit 3 "# 3. added the minimal HTML tags"

# Create new branch for Development
$GIT branch DEV
$GIT switch DEV

make_commit 4 "# 4. added text for page title"

make_commit 5 "# 5. modified text specifically for 3308"

make_commit 6 "# 6.  added text to be changed by student"

# Create new branch for student TASKS
$GIT branch TASKS

# BUT first add logo on DEV branch, make sure we are in the DEV branch
$GIT switch DEV

make_commit 7 "# 7. added CU logo "

# add tasks in TASKS branch
$GIT switch TASKS

make_commit 8 "# 8.  added student tasks"

make_commit 9 "# 9.  updated the task instructions"

# add change to MAIN branch
$GIT switch MAIN

make_commit 10 "#10. show a comment tag, capitalized words"

# add another logo to DEV branch
$GIT switch DEV
make_commit 11 "#11. added  3308 logo"

echo ""
