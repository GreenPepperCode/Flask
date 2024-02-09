# views.py
from flask import render_template, jsonify, session, request, redirect, url_for, flash
from .models import User, Post
import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Vérifiez les informations d'identification de l'utilisateur
        # Si les informations d'identification sont valides, récupérez l'utilisateur depuis la base de données
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            session['user_id'] = user.id  # Stockez l'ID de l'utilisateur dans la session
            return redirect(url_for('user'))  # Redirigez l'utilisateur vers sa page utilisateur
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect.')
    return render_template('login.html')

# Définissez une route pour la déconnexion
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Supprimez l'ID de l'utilisateur de la session
    return redirect(url_for('index'))  # Redirigez l'utilisateur vers la page d'accueil


@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/api/posts')
def get_posts():
    posts = Post.query.all()
    return jsonify([post.serialize() for post in posts])
