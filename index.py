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


@app.route('/crud')
def crud():
    return render_template('crud.html')


@app.route('/crud/get', methods=['GET', 'POST'])
def crud_get():
    id = request.args.get('id')
    for post in posts:
        if str(post['id']) == str(id):
            return render_template('crud.html', post=post)
    return "Post not found"


@app.route('/crud/delete', methods=['GET', 'POST'])
def crud_delete():
    id = request.args.get('id')
    for post in posts:
        if str(post['id']) == str(id):
            posts.remove(post)
            return "Post deleted " + str(id)
    return "Post not found"


@app.route('/crud/put', methods=['GET', 'POST'])
def crud_put():
    id = request.args.get('id')
    for post in posts:
        if str(post['id']) == str(id):
            post['author'] = "Updated"
            post['title'] = "Updated"
            post['content'] = "Updated"
            return "Post updated " + str(id)
    return "Post not found"


@app.route('/crud/post', methods=['POST'])
def crud_post():
    if request.method == 'POST':
        id = request.form['id']
        for post in posts:
            if str(post['id']) == str(id):
                return "Post already exists " + str(id)
        new_post = {}
        new_post['author'] = "Posted"
        new_post['title'] = "Posted"
        new_post['content'] = "Posted"
        new_post['id'] = str(id)
        posts.append(new_post)
        return "Post posted " + str(id)


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


@app.route('/add_likes/<id>', methods=['POST'])
def add_like(id):
    for post in posts:
        if str(post['id']) == str(id):
            post['likes'] += 1
    return redirect('/')


@app.route('/add_dislikes/<id>', methods=['POST'])
def add_dislike(id):
    for post in posts:
        if str(post['id']) == str(id):
            print(post)
            post['dislikes'] += 1
    return redirect('/')


if __name__ == '__main__':
    app.debug = True
    app.run()
