from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    largest = None
    if request.method == 'POST':
        largest = None
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        num3 = float(request.form['num3'])
        if num1 > num2 and num1 > num3:
            largest = num1
        elif num2 > num1 and num2 > num3:
            largest = num2
        else:
            largest = num3

    largest = format(largest, '.2f')

    return render_template('index.html', largest=largest)

if __name__ == '__main__':
    app.run(debug=True)

