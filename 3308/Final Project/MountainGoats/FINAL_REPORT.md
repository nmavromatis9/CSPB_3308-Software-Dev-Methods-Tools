# Group 5 (MountainGoats) Medical Procedure Price Checker Project
#### Members
- Nicolas Mavromatis, nmavromatis9, nima6629@colorado.edu
- Patrick Chesnut, chesnutpc, patrick.chesnut@colorado.edu
- Cooper Ide, cjide13, coid6456@colorado.edu

Project Tracker Link: https://trello.com/b/T4HiUfEx/project-management

Version Control Repository: https://github.com/cjide13/MountainGoats

Demonstration Video Link: https://youtu.be/uK0iifxkAAM

Link to Deployment Site: https://mountaingoat.onrender.com/

Test Cases: https://github.com/cjide13/MountainGoats/blob/main/tests.py

#### Final Status Report:

The goal of this project was to create a functional medical procedure price checker. Recently, executive orders were issued directing the Centers for Medicare and Medicaid services to promulgate regulations mandating that all medical procedure prices be made available by hospitals as machine readable formats. We thus wanted to create a sample web app that searches for prices by hospital, insurer, or test and generates price tables dynamically, and which allows the user to browse all the available options by category. We also wanted to implement a basic login, user preference, and admin interface to update prices. This would require integration of HTML, JS, CSS, Flask, SQL, and a hosting website. 

We completed all of our major goals for the project. We created a simple medical procedure database out of machine readable JSON files. The website app is fully functional, with search bars for every category (Procedure/CPT code, hospital, insurer) that work by querying the database then generating HTML tables dynamically. There are also browse by links for every category, created by SQL searches that generate the links and tables dynamically. There is a basic login, logout, signup, and signout system and basic user information. The user information allows the user to update and save preferred provider, hospital, and doctor.  Bootstrap was implemented to create a pleasant UI. Lastly, an admin page is functional which allows the user to update a price for a specific test, which is then saved to the database.

We completed everything we began implementing.

We planned to possibly have an interactive map for each hospital region, but we knew this was a very optional long-shot goal, to be saved only if we had a lot of extra time. Another possible improvement would be to expand the database to have more entries, and upgrade to a SQL framework that works better for larger databases than SQLite. Also, we planned to have an autocomplete functionality for the search bar, which would use a Trie data structure. However, we were a smaller than normal group, working on balancing learning many new frameworks and implementing the project in a limited time frame, so we were not able to add these extra features.

There are no known problems or bugs that we are aware of. 
