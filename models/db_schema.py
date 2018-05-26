from app import db
from sqlalchemy_utils import PasswordType
import datetime


class Sessions(db.Model):
    session_token = db.Column(db.VARCHAR, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    csrf_token = db.Column(db.VARCHAR, nullable=True)
    created = db.Column(db.DATETIME, nullable=False, default=datetime.datetime.now)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR, nullable=False)
    email = db.Column(db.VARCHAR)
    password = db.Column(PasswordType(schemes=['pbkdf2_sha512']), nullable=False)
    salt = db.Column(db.VARCHAR, nullable=False)


r_widgets = db.Table('r_widgets',
                     db.Column('dashboard_id', db.Integer, db.ForeignKey('dashboards.id'), primary_key=True),
                     db.Column('widget_id', db.Integer, db.ForeignKey('widgets.id'), primary_key=True)
                     )


class Dashboards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)
    widgets =  db.relationship("Widgets", secondary=r_widgets, lazy='subquery',
                                   backref=db.backref('dashboard_id', lazy=True))


class Widgets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR, nullable=False)
    type = db.Column(db.VARCHAR, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    options = db.Column(db.VARCHAR)
