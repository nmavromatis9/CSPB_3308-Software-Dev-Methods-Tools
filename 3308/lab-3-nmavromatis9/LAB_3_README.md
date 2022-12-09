# CSPB-3308  Lab 3 :  Team Meeting (Agile Sizing) 
<figure width=100%>
  <IMG SRC="https://www.colorado.edu/cs/profiles/express/themes/cuspirit/logo.png" WIDTH=100 ALIGN="right">
</figure>

There are two parts to this assignment: team and individual.  The team will arrange a meeting time, perform sizing of feature requests,  and design acceptance criteria for those feature requests.   Each individual team member will also continue to create scripts and programs to aid the extraction of data for a project.
<hr>

## Part 1 - Team Activity
### Step 1 : Creating a Meeting Time
Schedule a zoom meeting where all members of your team will be present.

If you cannot arrange a meeting, private post in Piazza (PM) your instructor and we can try to work out other arrangements. 

<img src="images/deliverable.png" alt="Deliverable Item" WIDTH=40 ALIGN="left" />
When you have set the day/time for your meeting, PM the instructor with your team number and the planned date/time for the meeting.
Record the meeting using Zoom! Ask the instructor for help if there are problems getting zoom to work for you.

### Step 2 : Elect a Scrum master
Elect a scrum master for your team. 
You need to elect someone to manage the meetings.  During the semester you may want to change the scrum master between team members.  However, for any given week or sprint, the scrum master should remain the same. 

__What best describes a scrum master?__
In simple terms, the Scrum Master can be defined as the servant-leader of the Scrum Team. The individual is responsible for ensuring that the team adheres to the theory, practices, and rules of set forth in your management framework.Other names for the scrum master include servant leader, coach, or facilitator. Despite using the term “master,” the person in this role does not have the authority to make strategic or substantive decisions about the project.  They are there to make sure your meetings stay focused and productive. 

 There are other roles that need to be filled in an Agile team.  It is possible to share or trade roles throughout the project.

<img src="images/deliverable.png" alt="Deliverable Item" WIDTH=40 ALIGN="left" /> 

### Have your elected scrum master PM the instructor to get a list of **User Stories** that you will need to address in the next step.

<hr>
<br>

### Step 3 : For each user story : estimate the size of the effort needed
Create document to capture summary of effort levels in a unitless estimation.
You will be practicing Agile sizing of **User Stories**.

#### Practice Planning Poker
Your estimations of effort are in unitless amounts.  The levels represent a relative difficulty, not an absolute unit.   Planning Poker uses "cards" with labels: 1, 2, 3, 5, 8, 13, 20, ?.  So a story with effort level 8 should be about four times harder to implement than a story with effort level 2. "?" means "I have no idea".

**For each story:**
   1. The Scrum master reads aloud a single single user story.
   2. The team members (including scrum master) each privately "pick a card" (maybe write your number on a piece of paper).
   1. All team members reveal their choice simultaneously.
   1. If the numbers are all the same
   
       * record your estimation 
       * move to the next user story.
   1. If the numbers are NOT all the same, 

       * discuss the effort required
	   * start by having the highest and lowest voters explain their reasoning
       * discuss the story together as a team
       * GOTO step 2
* It is okay if it takes several rounds of voting for each user story. 
* Avoid just "averaging" the scores, let each person make their best judgment and communicate their thinking.


<hr>

### Step 4 : For each user story: Create Acceptance Criteria
Add acceptance criteria to each user story in a summary document of this planning step.

<img src="images/deliverable.png" alt="Deliverable Item" WIDTH=40 ALIGN="left" />
Each **User Story** provides an informal, natural language description of a feature of the software or product from an end-user perspective.  You have been provided with a set of **User Stories** for your team.  Each user story has specific information.  The user role, the description of desired behavior,  and the outcome or reason the feature is being requested are provided for you.
As a team, you will evaluate the story and provide a set of criteria that could be used to validate the feature.

```
User Story Card
______________________________________________________________________________
As a 	: <user role>
I want	: <description of desired behavior>
So that : <reason for desired behavior / what you get from it>

Effort
Level	: <level of effort : dimensionless units>

Acceptance Criteria
Given	: 	<context of action>
When 	: 	<some action is completed>
Then 	: 	<set of observable outcomes>
____________________________________________________________________________

```

<img src="images/deliverable.png" alt="Deliverable Item" WIDTH=40 ALIGN="left" />

Your team will create a document with the user stories, the effort level determined by the group, and the set of acceptance criteria.  The document should be a markdown document and the cards can be copied from the information given to the scrum master. 

Once the team has completed the creation of the document, each memeber will add the document to their local assignment repository.  Step 4 is complete once the document is **committed** and **pushed** to the remote classroom repository.

Document format for Part 1:

   * Team Number
   * Team Name
   * Team Members in meeting
   * Link to Zoom recording
   * List of User Stories with 
	   * effort level 
	   * a set of acceptance criteria.  
	   * Each User Story will have the format listed above.


<hr>

### Step 5 : Determine a weekly day/time to meet to discuss the project

Find a permament day and time for your weekly meeting.  You should schedule up to an hour of time, but often you can complete the full team meeting in a half hour.  Let the team members take lengthy discussions that only concern some of the team,  offline or moved to another scheduled meeting.  

Use the weekly meeting to quickly let each team member say: 

 * What was accomplished in the previous week?
 * What is planned for the next week?
 * What impediments stand in your way of accomplishing them?
<br><br>

<img src="images/deliverable.png" alt="Deliverable Item" WIDTH=40 ALIGN="left" />
Step 5 is completed when you send a PM to the instructor with 
your team # and the scheduled time for your meetings.
<br><br>
<hr>
<hr>

## Part 2 : Individual Activity
You will continue to write scripts to perform more complex tasks.

<img src="images/deliverable.png" alt="Deliverable Item" WIDTH=40 ALIGN="left" />
1. Write a script to create the correct subdirectories in the storage hierarchy and download a specific HTML file from the Jarchive website.  The script will be given two parameters for the `year` and the `game id` to be downloaded.  The parameters should be check for validity (both parameters must be all digits, year should be within range of when games were broadcast).
<br><br>

<img src="images/deliverable.png" alt="Deliverable Item" WIDTH=40 ALIGN="left" />
2. Write script to create the extracted data files for a given `year` and `game id`.  The parameters should be validated by assuring that the directories exist and that an HTML file is available in that directory.

<hr>

### You have completed the Lab-3 tutorial.  
<img src="images/deliverable.png" alt="Deliverable Item" WIDTH=40 ALIGN="left" />
Although the grading will be done by accessing your Git Classroom remote repository, <br>
each team member must submit the following to Moodle Assignment:
   * Team Activity
      * Team Number
      * Team Name
      * Team Members in meeting
      * Link to Zoom recording
      * Filename of User Story document in your repository  (include path if not at top level)
	
   * Individual Activity
      * Filename for script 1
      * Filename for script 2
      * Number of hours required to implement scripts
	

**IMPORTANT**: Make sure that all your added files and changes are **pushed** to the remote repository before going to Moodle to submit your completion information in the Moodle assignment.

Here is what you should have accomplished:
	
	1. Had a team meeting to size the effort of **user stories*
	2. Created a document listing the story and the effort estimation
	3. Added acceptance criteria for all the user stories
	4. You have established a weekly meeting time
	
<hr><hr><hr>

