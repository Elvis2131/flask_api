from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

@auth.post('/register')
def register_user():
    return "User created!"

@auth.get('/user')
def get_user():
    return "User"