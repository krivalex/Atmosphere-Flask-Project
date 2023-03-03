from flask import Flask
from flask import render_template
from data import posts
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/home')
def home_video():
    return render_template('index.html')


@app.route('/calculate')
def calculate():
    return render_template('calculate.html', posts=posts)


if __name__ == '__main__':
    app.debug = True
    app.run()
