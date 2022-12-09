# CSPB-3308  Lab 6 :  Flask Tutorial
<figure width=100%>
  <IMG SRC="https://www.colorado.edu/cs/profiles/express/themes/cuspirit/logo.png" WIDTH=100 ALIGN="right">
</figure>
<hr>
Flask is a web framework, which means it provides you with tools, libraries and technologies that allow you to build a web application. The web application can be as simple as a few web pages, a blog, a wiki, or as complex as a full web application with dynamic pages and access to database data.   

Flask is a micro-framework that is written in Python. It is classified as a micro-framework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components, but there are many third-party libraries provide common functions.
One of the drawbacks of a light weight framework is that you will have to do more work on your own.  This is good when doing school projects, but may become cumbersome if you are working to create a complex website (100's of pages)

Flask is a back-end framework, which means that it provides the technologies, tools, and modules that can be used to build the functional rendering of pages of the web app rather than the design or look of it. Flask is considered one of the easiest frameworks to learn for beginners.    
<hr>

<img src="images/construction-set-icon.jpg" alt="Under Construction" WIDTH=120 ALIGN="left" />

### This lab is still under construction.  
 
 Please report all speeling and grammered issues.<br>
 Also let us know about any unclear descriptions of work to be performed. 
 <br><br><br>
<hr>

In this lab you will be installing the Flask application, setting up your environment to run a web service, and writing the code to render web pages in your browser.
This is an individual project where each student will create a basic web server and support a number of independent web pages. 
 
You can install Flask in a virtual environment on your local system or on the **CSEL.io** jupyterHub virtual machine.   If you will be working in the **CSEL.io** environment, there are a few extra steps to setup the Flask pages to be accessed in your local browser while getting information from the virtual machine.

Here are descriptions of the files in the lab repository:
```
.
├── images
│   ├── card.png
│   └── deliverable.png
├── example.tar.gz
├── LAB_6_README.md
└── README.md
```
 
|Filename | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description |
|--- |--- |--- |
| images || directory with images for the README files |
| example.tar.gz || compressed directory containing files to run web service on CSEL.io virtual machine with access from local browser |
| LAB_6_README.md || description of the lab steps and deliverables |
| README.md | | generic instructions |
 
 
Please install Flask on the machine of your choice and work through the Flask Quickstart tutorial up through the section "Render Templates".

<hr>

### Step 1 : Creating a Virtual Environment and Installing Flask
You will be installing the Flask application.  Depending on which system, Python, and currently installed utilities, you may be installing different versions of Flask. Sometimes you need to run two different sets of applications, but need to isolate them as if they were the only version on the system.
 
A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed on a computer.
A virtual environment is a directory tree which contains Python executable files and other files which indicate that it is a virtual environment.  Once you activate a virtual environment, any installations will occur only in that virtual environment.  

 
Create a Virtual Environment as described in the videos.  Creating a new virtual environment is also reviewed in the Flask Installation guide. 
<span style="color:red">Make sure to create your virtual environment OUTSIDE of the lab repository.</span>  The virtual environment can be very large depending on the set of utilities and application that are installed.  These can be hundreds of megabytes of data that SHOULD NOT be stored in your repository.   The virtual environment is usually created in the directory above where you store your cloned repositories.
 
Once a virtual environment has been created, it can be “activated” using a script in the virtual environment’s binary directory. The invocation of the script `<venv>/bin/activate` is platform-specific (`<venv>` must be replaced by the path of the directory containing the virtual environment).

When a virtual environment is active, the VIRTUAL_ENV environment variable is set to the path of the virtual environment. This can be used to check if one is running inside a virtual environment.  All scripts or applications will first check the Python virtual environment to find the files.  You can run all your commands without needing to know which environment is currently active.

You can deactivate a virtual environment by typing “deactivate” in your shell. The exact mechanism is platform-specific and is an internal implementation detail (typically a script or shell function will be used).

##### Follow the virtual environment setup procedure and Flask installation described in:
     https://flask.palletsprojects.com/en/2.2.x/installation/#installation
 
<span style="color:red">Remember that you DO NOT include your virtual environment in the repository.</span>  It adds unneeded and unwanted megabytes to the repository.
<hr>
 
### Step 2 : Creating Web Service and Routes from the Flask Tutorial

Work through the Flask Quickstart tutorial up through the section "Rendering Templates" in the Flask Tutorial.  Feel free to read through the rest of the tutorial and implement any of the samples.  Only the routes described in the tutorial up to and including the **Rendering Templates** are required.

     https://flask.palletsprojects.com/en/2.2.x/quickstart/

Complete the steps of the tutorial through the **Variable Rules** section.  
 
If you are running the Flask application on your **CSEL.io** virtual machine, you will need to use a slightly different web address to see your pages in the first part of the tutorial.
You will also need to complete Step 3 before continuing with the tutorial.
 
To access the Flask web server you need to use the following modification.  Normally, you can access the web service on your local machine with `127.0.0.1:5000`  or `localhost:5000`, where the `5000` is the port number being used by Flask.
 
To access the pages when you are running the web service on the *CSEL.io* Virtual Machine, use the following address: `https://coding.CSEL.io/user/<user name>/proxy/5000`.  Again, the `5000` is the port your Flask application is using.  The `<user name>` is replaced with your user name used by the *CSEL.io* system.  Look at the address field when you are in a browser window for the virtual machine.  You will probably see your CU Id in the address.  That is the value that you replace in the web address listed above.
 
You will create a number of routes while completing the tutorial.  Below is a list of the routes that you should have created up to this point in the tutorial:

##### Required Routes from Flask Tutorial for Lab
```
1. static text page, "index"   @app.route('/')
2. static text page, "hello"   @app.route('/hello')
3. static text page, "project" @app.route('/projects/')
4. static text page, "about"   @app.route('/about')
5. dynamic text, route parameter, string  @app.route('/user/<username>')
6. dynamic text, route parameter, int     @app.route('/post/<int:post_id>')
7. dynamic text, route parameter, subpath @app.route('/path/<path:subpath>')
```
<hr>
 
### Step 3: Modifications needed to access files on *CSEL.io* virtual machine in Local Browser 
 
The files on the virtual machines use for the course are not normally available to the outside world.  But there are times you want to share files.  For example, if you are running a web service on your CSEL.io virtual machine and you are using a browser to display information, you will probably want to access stylesheets, graphic images,  and other local files.

This requires that we modify the basic Flask application to use a prefix that will allow read access to virtual machine files.

Included in the Lab repository is a compressed file containing the following structure:
```
├── example
    ├── prefix.py
    ├── setup.sh
    ├── static
    │   └── css
    │       └── prefix.css
    └── templates
        ├── prefix_test.html
        └── route_not_found.html
```
 
|Filename | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description |
|--- |--- |--- |
| prefix.py || Contains the main Flask web site description.  Contains a required function `PrefixMiddleware()` that will handle the indirection required to access files from the CSEL.io virtual machine on your local browser. See description below for use of the required routine. |
| setup.sh || This script provides `bash` shell with setting that Flask will use to setup its functionality.  Includes settings to help debug your page rendering. |
| static || Directory to hold the static files used in web pages.  The `css` directory is used to store the *Cascading Style Sheets* used to modify the format of a page content.  We have provided a sample file to test the browser access to VM files. |
| templates | | Directory to hold the templates that are used to generate the web pages.  These templates are generic HTML files that specify locations to insert dynamic data.  |

The following code is required to make the remote virtual machine files available to the local web browser.   You should be able to copy this into your Flask project file to enable the access.  Notice that there is a function and a call to your `app` Flask object to install that function into the Flask processing.

 ```
###############################################################################
## This section allows us to set the prefix information to access
## url's that access our JupyterHub environment.
##
## Every call to url_for will be given the prefix for accessing via PROXY.
## Before releasing this to an external site or use in your local machine, 
## make the 'SCRIPT_NAME' an empty string.
##

class PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        # set the prefix for all url to the Jupyterhub URL for my virtual machine
        # this path is set to my user [KNOX] and port [3308] 
        # (see the code at bottom to see how port is set to 3308 instead of 5000)
        environ['SCRIPT_NAME'] = "/user/knoxd/proxy/3308/" 
       
        # call the default processing
        return self.app(environ, start_response)

# insert our proxy setting url class as wrapper to the app
app.wsgi_app = PrefixMiddleware(app.wsgi_app)
```

Also notice that there is a user name that is hard coded into the prefix string.  You must replace my user name with your own user name.  
 
The last thing to notice is the use of a different `port` than the default port 5000.  The port is essentially a mailbox on a computer to which other application can talk to the computer.  Flask by default uses port 5000 for the browser to request web pages.  Other applications use other port numbers.   Usually for this course, I specify that Flask should use the port 3308, so that I know all requests on that port will be for this course.
 
You must use the same number in this routine as is being specified in the Flask setup.  See the `setup.sh` and the end of the `prefix.py` files for how to specify the port number to the  Flask application.
<hr>

### Step 4: Continue the Tutorial through the *Rendering Templates* section
If your website contains only few pages, changing its style will take you some time but is doable. However, if you have a lot of pages (for example, the list of items you sell in your store), this task becomes overwhelming.

Using templates you are able to set a basic layout for your pages and mention which element will change. This way you can define your header once and keep it consistent over all the pages of your website, and if you need to change your header, you will only have to update it in one place.

Using a template engine will save you a lot of time when creating your application, but also when updating and maintaining it. See a quick introduction to templates here: [How To Use Templates In A Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application)
 
<img src="images/deliverable.png" alt="Deliverable Item" WIDTH=40 ALIGN="left" />
flask.py file containing routes described in Flask tutorial.

##### Required Routes from Flask Tutorial
```
1. static text page, "index"   @app.route('/')
2. static text page, "hello"   @app.route('/hello')
3. static text page, "project" @app.route('/projects/')
4. static text page, "about"   @app.route('/about')
5. dynamic text, route parameter, string  @app.route('/user/<username>')
6. dynamic text, route parameter, int     @app.route('/post/<int:post_id>')
7. dynamic text, route parameter, subpath @app.route('/path/<path:subpath>')
8. methods for GET and POST, @app.route('/login', methods=['GET', 'POST'])
9. render template,  @app.route('/hello/<name>'), render_template('hello.html', name=name)
```
<br><br>
<hr>

### Step 4 : Creating Custom Routes

Below is a list of possible custom routes that you can create. The number in parentheses is the relative amount of effort required (as in Agile task sizing) to create the route.
You must select a set of custom routes to implement.   The total work effort for this individual sprint is 10.  Select a set of routes that add up to 8-10.  The more difficult ones require programming the creation of HTML structures on the page.  This will take more time as you need to learn a bit more HTML (before we get to it in the course).

```
(1) static text page, “index” with list of available pages
(1) static text, read from text file using static filename
(1) static text, read from text file using parameter filename
(1) static HTML, read from file containing HTML using static filename
(2) static HTML, read from file containing HTML using parameter filename
(2) dynamic text, r/w file (counter)
(3) dynamic text, results of system call (e.g. text = os.system(cmd), where cmd is command line string)
(2) dynamic text, form data (name/value pairs in URL)
(3) dynamic HTML, render
(2) static HTML display a list
(2) dynamic HTML, list contains values to display
(2) static HTML, table, static data
(3) dynamic HTML, table from list of data
(3) dynamic HTML, table from data file
(2) error handler for 404 error (see Flask tutorial: “Redirects and Errors”)
``` 

 
<img src="images/deliverable.png" alt="Deliverable Item" WIDTH=40 ALIGN="left" />
flask.py file containing custom routes that you have created.  Make sure to comment each route to indicate which of the items that route is implementing.
 
Here are a couple ideas for a selection of routes to consider:

| Group 1 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Group 2|
|--- |--- |--- |
|(1) static text, read from text file using parameter filename || (1) static text page, “index” with list of available pages|
|(1) static text, read from text file using static filename ||(1) static HTML, read from file containing HTML using static filename|
|(2) static HTML, read from file containing HTML using parameter filename ||(2) error handler for 404 error (see Flask tutorial: “Redirects and Errors”)|
|(3) dynamic HTML, table from list of data ||(2) dynamic text, r/w file (counter)|
|(3) dynamic HTML, table from data file ||(2) dynamic text, form data (name/value pairs in URL)|
|||(2) static HTML, table, static data |
 
<br><br>
<hr>

<hr>

### You have completed Lab-6
    
Here is what you should have accomplished:
	
	1. Created a virtual environment with Flask installed (not in the repository)
	2. Created the routes described in the Flask Tutorial
	3. Created a set of custom routes for your web site (comments in code describe each route's purpose)

##### You should have approximately the following structure in your project (your flies will vary depending on your implementations):
```
.
├── flask.py (containing both required and custom routes)
├── images
│   ├── . . .
│   ├── card.png
│   └── deliverable.png
├── setup.sh (optional)
├── static
│   ├── . . .
│   ├── my_static.png
│   └── my_static.txt
│── templates
│   ├── . . .
│   └── hello.html
├── LAB_6_README.md
└── README.md

```
 
<img src="images/deliverable.png" alt="Deliverable Item" WIDTH=40 ALIGN="left" />
Although the grading will be done by accessing your Git Classroom remote repository, <br>
you must submit the following to Moodle Assignment:

    * Your name:
    * CU ID: (4 letters - 4 digits)
    * GitHub Username:
    * hours to complete lab:


**IMPORTANT**: Make sure that all your added files and changes are **pushed** to the remote repository before going to Moodle to submit your lab completion information in the Moodle assignment.

<hr><hr><hr>

