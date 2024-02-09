from app import db  # Importez l'instance db de votre fichier app.py
from datetime import datetime  # Importez datetime pour utiliser la fonction utcnow

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(64))
    usermail = db.Column(db.String(120), unique=True)
    userlogin = db.Column(db.String(64), unique=True)
    pseudo = db.Column(db.String(64), index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
