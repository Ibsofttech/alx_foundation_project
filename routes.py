from flask import render_template, redirect, url_for, request
from app import app, db
from models import User, Lesson, Quiz
from flask_login import login_user, login_required, logout_user, current_user

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/lessons/<int:id>')
@login_required
def lesson(id):
    lesson = Lesson.query.get_or_404(id)
    return render_template('lesson.html', lesson=lesson)

@app.route('/quiz/<int:lesson_id>', methods=['GET', 'POST'])
@login_required
def quiz(lesson_id):
    quiz = Quiz.query.filter_by(lesson_id=lesson_id).all()
    if request.method == 'POST':
        # handle quiz submission
        pass
    return render_template('quiz.html', quiz=quiz)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # login logic here
        pass
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # registration logic here
        pass
    return render_template('register.html')
