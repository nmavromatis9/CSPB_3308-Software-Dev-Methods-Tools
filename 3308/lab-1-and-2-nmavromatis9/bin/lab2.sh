#/bin/sh

# You must edit and remane this file file for your use
# It is included to make sure your text is correct for 
# grading your output
#
# Usage to run the script:
#  <script_name> <filename>

#Nicolas Mavromatis
#8/26/22
#nima6629
#This script is to learn and practice Regex.
#Note that often -E extended is used, where special characters exist as such without /
#In basic -e the chars ?, +,  {,  |, (, )  must be backslashed to be special
#In extended, these same symbols must be backslashed to be literal chars
#NOTE: Use \ NOT /. This was a major bug I wasted time on.


# How many lines in the data file?
echo ""
echo -n "How many lines in the data file?    "
wc -l $1

# How many lines start with Capital Letter?
echo ""
echo -n "How many lines start with Capital Letter?    "
grep -e "^[A-Z]" $1| wc -l

###
### Insert your solution to each problem
###

# How many lines end with a number?
echo ""
echo -n "How many lines end with a Number?    "
grep -e "[0-9]$" $1|wc -l

# How many lines do not start with a vowel?
echo ""
echo -n "How many lines do not start with a vowel?   "
grep -E "^[^aeiouAEIOU]" $1|wc -l

# How many 12 letter (alphabet only) lines?
echo ""
echo -n "How many 12 letter (alphabet only) lines?    "
grep -E "^[a-zA-Z]{12}$" $1|wc -l

# How many phone numbers are in the dataset (format: _ _ _-_ _ _-_ _ _ _)?
echo ""
echo -n "How many phone numbers are in the dataset (format: _ _ _-_ _ _-_ _ _ _)?    "
grep -E "^[0-9]{3}-[0-9]{3}-[0-9]{4}$" $1|wc -l 
#echo -n "    when allowing for '(xxx)xxx-xxxx'    :  "
#grep -E "^\(?[0-9]{3}(\)|-)[0-9]{3}-[0-9]{4}$" $1|wc -l
#echo -n "    when only checking for 'xxx-xxxx'    :  "
#grep -E "[0-9]{3}-[0-9]{4}" $1|wc -l


# How many phone numbers have area code the same as University of Colorado Boulder, "303"?
echo ""
echo -n "How many 303 phone numbers?   "
grep -E "^\(?303(\)|-)[0-9]{3}-[0-9]{4}$" $1|wc -l
#echo -n "  when only allowing for '303-xxx-xxxx'    :   "
#grep -E "^303-[0-9]{3}-[0-9]{4}$" $1|wc -l


# How many begin with a vowel and end with a number?
echo ""
echo -n "How many begin with a vowel and end with a number?    "
grep -E "^[aeiouAEIOU].*[0-9]$" $1|wc -l

# How many email addresses are from geocities? (Eg: end with'geocities.com')?
echo ""
echo -n "How many email addresses are from geocities? (Eg: end with\'geocities.com\')?    "
grep -E "geocities.com$" $1|wc -l

# How many email addresses are in ‘first.last’ name format and involve someone who’s 
# first name starts with a letter in the first half of the alphabet?
echo ""
echo "How many email addresses are in ‘first.last’ name format and involve someone "
echo -n "who’s first name starts with a letter in the first half of the alphabet?      "
grep -E "^[A-M][a-z]*\.[a-zA-Z]*@" $1|wc -l

echo ""

# Running regexAnswers.sh script file should output 10 lines which is the result of wc –l for each regex command. 
# If unsure of any one of the answers, use echo "0" so that the rest of your answers align in the output.

