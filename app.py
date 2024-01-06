# import the request module from flask
from flask import Flask, render_template, request

app = Flask(__name__)


# to get the data from the form we need to use the request object
# lets add a methods argument to the route decorator
@app.route('/', methods=['GET', 'POST'])
def index():
    # define a variable to hold the largest number
    largest = None
    # define a variable to hold the messagee'
    # logic:
    # 1. check if the request method is post (basically checked if the form is submitted)
    if request.method == 'POST':
        # 2. get the numbers data from the form with request object using request.form
        num1 = request.form['num1']
        num2 = request.form['num2']
        num3 = request.form['num3']
        # compare the numbers to find the largest
        if num1 > num2 and num1 > num3:
            largest = num1
        elif num2 > num1 and num2 > num3:
            largest = num2
        else:
            largest = num3
        # set the message

    # render the template with the largest and the message
    return render_template('index.html', largest=largest)

if __name__ == '__main__':
    app.run(debug=True)

