from blogapp import app, db, bcrypt
from flask import render_template, flash, redirect, url_for, request
from blogapp.forms import RegForm, LogForm, PostForm
from blogapp.models import User, Post
from flask_login import login_user, logout_user, current_user


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title = 'Home')

@app.route('/posts')
def posts():
    posts = Post.query.all()
    if posts is not None:
        return render_template('posts.html', title='Posts', posts=posts)
    else:
        return '<h1>No posts</h1>'

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegForm()
    if form.validate_on_submit():
        userm = User.query.filter_by(email=form.email.data).first()
        usern = User.query.filter_by(username=form.username.data).first()
        if userm is None and usern is None:
            hashedPassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            newUser = User(username=form.username.data, email=form.email.data, password=hashedPassword)
            db.session.add(newUser)
            db.session.commit()
            flash('Account created successfully', 'success')
            return redirect(url_for('login'))
        else:
            flash('Account with that name or email already exists', 'danger')
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LogForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/posts/new', methods=['GET','POST'])
def newpost():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post has been submited', 'success')
        return redirect(url_for('posts'))
    return render_template('newpost.html', title='New post', form=form)