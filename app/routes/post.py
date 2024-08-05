from flask import Blueprint, render_template, request, redirect
from ..extensions import db
from ..models.post import Post

post = Blueprint('post', __name__)


@post.route('/', methods=['GET', 'POST'])
def all():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template('post/all.html', posts=posts)


@post.route('/post/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        teacher = request.form['teacher']
        subject = request.form['subject']
        student = request.form['student']
        post = Post(teacher=teacher, subject=subject, student=student)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(str(e))
    else:
        return render_template('post/create.html')


@post.route('/post/<int:id>/update', methods=['POST', 'GET'])
def update(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        post.teacher = request.form.get('teacher')
        post.subject = request.form.get('subject')
        post.student = request.form.get('student')
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(str(e))
    else:
        return render_template('post/update.html', post=post)


@post.route('/post/<int:id>/delete', methods=['POST', 'GET'])
def delete(id):
    post = Post.query.get_or_404(id)
    try:
        db.session.delete(post)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(str(e))
        return str(e)