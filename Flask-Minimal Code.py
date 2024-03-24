# First we  have to import the Flask class

# Next we have to create instance of this class. 
# The first argument is the name of the application’s module or package.
# If you are using a single module (as in this example), you should use app = Flask(__name__) .
# If you are creating multiple pakages or applications then for making debugging more simpler we can give app = Flask('yourapplication')

# We then use the route() decorator to tell Flask what URL should trigger our function.
# The function is given a name which is also used to generate URLs for that particular function,
# and returns the message we want to display in the user’s browser.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':
    app.run(debug=True)


# Finally we use the run() function to run the local server with our application.
#  The if __name__ == '__main__': makes sure the server only runs if the script is executed directly
#  from the Python interpreter and not used as an imported module.

#  debug = True will always provide simplest dedugging to your code with restarting your application.
# if you do not provide this, for every debugging you have to restart the flask server again and again.