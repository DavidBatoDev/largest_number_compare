# imports
from flask import Flask, render_template

# initialize the app by using flask
app = Flask(__name__)

# create a main route for the app to be displayed in the web
@app.route('/')
# render the html file for this app using a function
def index():
    return render_template('index.html')


# added a condition that runs the app and set the debugger to True for development
if __name__ == '__main__':
    app.run(debug=True)

