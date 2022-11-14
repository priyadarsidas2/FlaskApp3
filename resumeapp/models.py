from resumeapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from resumeapp.resume.redisdata import addValueToSet, addValueToHash, findLengthOfHash, findValueInHash

@login_manager.user_loader
def load_user(user_id):
    email = findValueInHash(user_id, "email")
    username = findValueInHash(user_id, "username")
    password_hash = findValueInHash(user_id, "password")
    category = findValueInHash(user_id, "category")
    return User(user_id, email, username, password_hash, category)

class User(UserMixin): #db.Model,
    """
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    """
    
    def __init__(self, id, email, username, password, category):
        self.id = id
        self.email = email
        self.username = username
        self.password_hash = password
        self.category = category
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    