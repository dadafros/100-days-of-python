from flask import Flask, render_template
from post import Post
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
response = response.json()
posts = {}
for post in response:
    posts[post["id"]] = Post(post["id"], post["title"], post["subtitle"], post["body"])

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    return render_template("post.html", post=posts[post_id])


if __name__ == "__main__":
    app.run(debug=True)
