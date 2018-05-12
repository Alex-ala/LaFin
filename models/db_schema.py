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
    widgets = db.relationship("Widgets", secondary=r_widgets, lazy='subquery',
                                   backref=db.backref('dashboard_id', lazy=True))


class Widgets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR, nullable=False)
    type = db.Column(db.VARCHAR, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    options = db.Column(db.VARCHAR(10000))


class Accounts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)
    currency_id = db.Column(db.Integer, db.ForeignKey('currencies.id'), nullable=False)
    account_number = db.Column(db.VARBINARY(250), nullable=False)
    BIC = db.Column(db.VARBINARY(64), nullable=True)
    name = db.Column(db.VARBINARY(256), nullable=False)
    IBAN = db.Column(db.VARBINARY(128), nullable=True)


class Currencies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(50), nullable=False)
    short = db.Column(db.VARCHAR(3), nullable=False)
    accuracy = db.Column(db.Integer, nullable=False)


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_valuta = db.Column(db.DATE, nullable=False)
    date_created = db.Column(db.DATETIME, nullable=False)
    description = db.Column(db.VARBINARY(1024), nullable=True)
    account_origin_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    account_target_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    amount = db.Column(db.VARBINARY(128),nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    reoccuring_template = db.Column(db.Integer, db.ForeignKey('reoccuring_transactions.id'), nullable=True)
