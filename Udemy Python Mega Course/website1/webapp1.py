from flask import Flask, render_template

# when this script is run as an application __name__ variable is set to __main__
# however if this script is imported to another script then __name__ is set to the scripts name e.g. webapp
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/about/')
def about():
    return render_template('about.html')


# this turns debuger mode on when run directly in python interpreter
if __name__ == "__main__":
    app.run(debug=True)