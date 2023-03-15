from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from data import posts
import random

app = Flask(__name__)


@app.route('/')
def calculate():
    return render_template('calculate.html', posts=posts)


@app.route('/add_card', methods=['POST'])
def add_card():
    # Get the data from the form using request.form
    author = request.form['author']
    title = request.form['title']
    content = request.form['content']
    id = random.randint(1, 100)
    date_posted = random.randint(1, 100)
    likes = 0
    dislikes = 0

    # Add the data to your array
    post_item = {
        'id': id,
        'author': author,
        'title': title,
        'content': content,
        'date_posted': date_posted,
        'likes': likes,
        'dislikes': dislikes
    }

    print(post_item)
    posts.append(post_item)

    # Redirect the user to some other page
    return redirect('/')


if __name__ == '__main__':
    app.debug = True
    app.run()
