from flask import Flask, request, render_template
from markupsafe import escape

#Nicolas Mavromatis, nima6629 Flask tutorial submission
#To access webpages:
#https://coding.CSEL.io/user/nima6629/proxy/3308
app = Flask(__name__)
################################################################
#Required Routes

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
#Functions for login
def show_the_login_form():
    return "This is a place holder for the login form."

def do_the_login():
    return "This is a placeholder for the login!"

#I needed to change the function name from hello to hello2 so there is no conflict
@app.route('/hello/')
@app.route('/hello/<name>')
def hello2(name=None):
    return render_template('hello.html', name=name)

###############################################################
#Custom Routes

#(1) static text, read from text file using static filename
@app.route('/text')
def text():
    with app.open_resource('static/text.txt', 'r') as f:
        return f.read()

#(1) static HTML, read from file containing HTML using static filename
@app.route('/readhtml')
def readhtml():
    with app.open_resource('static/readhtml.html', 'r') as f:
        return f.read()

#(2) static HTML, read from file containing HTML using parameter filename
@app.route('/dynamichtml/<hname>')
def dynamichtml(hname):
    html="static/"+hname+".html"
    with app.open_resource(html, 'r') as f:
        return f.read()

#(2) error handler for 404 error (see Flask tutorial: “Redirects and Errors”)
@app.errorhandler(404)
def page_not_found(error):
    return render_template('notfound.html', url=request.url), 404

#(2) static HTML display a list
@app.route('/list')
def list():
    with app.open_resource('static/list.html', 'r') as f:
        return f.read()

#(2) static HTML, table, static data
@app.route('/table')
def table():
    with app.open_resource('static/table.html', 'r') as f:
        return f.read()

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
       # this path is set to my user [nima6629] and port [3308]
       # (see the code at bottom to see how port is set to 3308 instead of 5000)
       environ[''] = "/user/nima6629/proxy/3308/"

       # call the default processing
       return self.app(environ, start_response)

# insert our proxy setting url class as wrapper to the app
app.wsgi_app = PrefixMiddleware(app.wsgi_app)
