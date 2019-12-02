from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)   
app.config['SECRET_KEY'] = 'LaKeyDeSecretta0rSomethingLikeThat'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

logManager = LoginManager(app)
logManager.login_view = 'login'
@logManager.user_loader
def user_loader(id):
    from blogapp.models import User
    return User.query.get(int(id))

from blogapp import routes