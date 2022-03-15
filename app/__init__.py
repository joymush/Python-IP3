from flask_sqlalchemy import SQLAlchemy
from ensurepip import bootstrap
import mailbox
from flask_bootstrap import Bootstrap
from flask import Flask
db = SQLAlchemy

bootstrap = Bootstrap()
app = Flask(__name__)
bootstrap.init_app(app)



bootstrap.init_app(app)
db.init_app(app)
mailbox.init_app(app)

from app import views