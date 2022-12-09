# CSPB-3308  Lab 5: Automated Unit Testing
<figure width=100%>
  <IMG SRC="https://www.colorado.edu/cs/profiles/express/themes/cuspirit/logo.png" WIDTH=100 ALIGN="right">
</figure>


**Unit Testing** is an extremely important aspect in development today.  Projects are large and developers will make many changes to the system.  It is mandatory that we are confident that new changes have not invalidated any of the code base.  This is done by providing a set of tests that are run against every version of the code base.  If a version of the code does not pass all the tests, it cannot be delivered to users.
    
  
**Unit Testing** is important and valuable for organizations. 
The testing and creation of tests to capture the possible bugs will simultaneously improve code quality and time to release. 
While there are no silver bullets in software development, effective unit tests can speed up development, testing, and even parts of functional requirements development process.
Good unit tests require the code be testable. When a developer knows that their code will be tested it improves the quality.
The tested code will have fewer defects, which means fewer bug fixes, which leads to faster project completion. 

<figure width=100%>
  <IMG SRC="images/unittest_1.png" WIDTH=50% ALIGN="LEFT">
</figure>
<hr>

This assignment assumes you have an understanding of unit testing. 
As a first step, please review the [Python 3 unittest framework documentation](https://docs.python.org/3/library/unittest.html).

    


**Objectives**
	
* Create test cases for a given Class Definition
* Create unit tests for each method
* Create a modified version of the implementation that passes all tests

<hr>

    
<div style="page-break-after: always"></div>
Project has following folder tree:
    
```
.  
├── code  
|   |── CharacterCounter.py
|   └── Test_CharacterCounter.py
├── images  
|   └── ...  
├── README.md  
└── LAB_5_README.md
```

| File | Description |
|---|---|
| images                  | directory holding images for README files |
| &nbsp;&nbsp;&nbsp;&nbsp;...        |  |
| code              | directory holding python files used in Lab-5. |
| &nbsp;&nbsp;&nbsp;&nbsp;CharacterCounter.py       | class definition to be used in Lab-5 |
| &nbsp;&nbsp;&nbsp;&nbsp;Test_CharacterCounter.py  | template for unit test |
| __README.md__           | __Readme file you are viewing here__ |
| LAB_5_README.md         | Readme file with Lab-5 instructions |

<hr>

### This assignment will focus on introducing you to test cases and automated unit testing.

All the information you need for this lab is in the [LAB_5_README](LAB_5_README.md).
<hr>

### When you have completed the Lab 
Your submission will consist of two items:
   * The modification of the Lab-5 repository by creating and/or updating source code. Remember that you must **push** your local repository changes to the remote repository. 
   * Submitting information to the assignment in Moodle.

We suggest that you **commit** and **push** your changes often.  Each time you complete a step of the Lab, **commit** the changes with the commit message indicating the step, and also **push** the changes to the remote repository.

**IMPORTANT**: Make sure that all your changes are **pushed** to the remote repository before going to Moodle to submit your completion information in the Moodle assignment.

Here is what you should have accomplished in Lab-5:
	
	1. Created test cases
	2. Created unit tests
	3. Resolved failed implementations
	
<hr><hr><hr>

