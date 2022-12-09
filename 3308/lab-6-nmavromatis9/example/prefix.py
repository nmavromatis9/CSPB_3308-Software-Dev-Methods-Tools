from flask import Flask, redirect, g, url_for, request, render_template, make_response
          
app = Flask(__name__)

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

###############################################################################
## simple routines to test parameters to the route method
##

@app.route('/')  
def index():
    return 'The URL for this page is {}'.format(url_for('index'))

@app.route('/prefix')
def prefix():
    return make_response(render_template("prefix_test.html"))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('route_not_found.html', url=request.url), 404


###############################################################################
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)
    