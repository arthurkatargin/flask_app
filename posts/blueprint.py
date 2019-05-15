from flask import Blueprint, render_template
from models import Post, Gost
from .forms import PostForm
from flask import request, redirect, url_for
from app import db
from flask_security import login_required

posts = Blueprint("posts", __name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Something wrong')

        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/<slug>/edit/', methods=['POST', 'GET'])
def edit_post(slug):
    global form
    post = Post.query.filter(Post.slug == slug).first()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))
    form = PostForm(obj=post)
    return render_template('posts/edit_post.html', post=post, form=form)


@posts.route('/')
def index():
    q = request.args.get('q')

    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    else:
        posts = Post.query.all()

    return render_template('posts/index.html', posts=posts)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    gosts = post.gosts
    return render_template('posts/post_detail.html', post=post, gosts=gosts)


@posts.route('/gost/<slug>')
def gost_detail(slug):
    gost = Gost.query.filter(Gost.slug == slug).first()
    posts = gost.posts
    return render_template('posts/gost_detail.html', gost=gost, posts=posts)
