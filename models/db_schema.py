import app
from sqlalchemy_utils import PasswordType
import datetime


class Sessions(app.db.Model):
    session_token = app.db.Column(app.db.VARCHAR, primary_key=True)
    user_id = app.db.Column(app.db.Integer, app.db.ForeignKey('users.id'), nullable=False)
    csrf_token = app.db.Column(app.db.VARCHAR, nullable=True)
    created = app.db.Column(app.db.DATETIME, nullable=False, default=datetime.datetime.now)


class Users(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True, autoincrement=True)
    name = app.db.Column(app.db.VARCHAR, nullable=False)
    email = app.db.Column(app.db.VARCHAR)
    password = app.db.Column(PasswordType(schemes=['pbkdf2_sha512']), nullable=False)
    salt = app.db.Column(app.db.VARCHAR, nullable=False)


r_widgets = app.db.Table('r_widgets',
                         app.db.Column('dashboard_id', app.db.Integer, app.db.ForeignKey('dashboards.id'),
                                       primary_key=True),
                         app.db.Column('widget_id', app.db.Integer, app.db.ForeignKey('widgets.id'), primary_key=True)
                     )


class Dashboards(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.VARCHAR, nullable=False)
    user_id = app.db.Column(app.db.Integer, app.db.ForeignKey('users.id'), nullable=False)
    widgets = app.db.relationship("Widgets", secondary=r_widgets, lazy='subquery',
                                  backref=app.db.backref('dashboard_id', lazy=True))


class Widgets(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.VARCHAR, nullable=False)
    type = app.db.Column(app.db.VARCHAR, nullable=False)
    user_id = app.db.Column(app.db.Integer, app.db.ForeignKey('users.id'), nullable=False)
    options = app.db.Column(app.db.VARCHAR(10000))


class Accounts(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    user_id = app.db.Column(app.db.Integer, app.db.ForeignKey('users.id'), nullable=False)
    currency_id = app.db.Column(app.db.Integer, app.db.ForeignKey('currencies.id'), nullable=False)
    account_number = app.db.Column(app.db.VARBINARY(250), nullable=False)
    BIC = app.db.Column(app.db.VARBINARY(64), nullable=True)
    name = app.db.Column(app.db.VARBINARY(256), nullable=False)
    IBAN = app.db.Column(app.db.VARBINARY(128), nullable=True)
    currency = app.db.relationship("Currencies")
    user = app.db.relationship("Users")


class Currencies(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.VARCHAR(50), nullable=False)
    short = app.db.Column(app.db.VARCHAR(3), nullable=False)
    accuracy = app.db.Column(app.db.Integer, nullable=False)


class Reoccurinig_transactions(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    date_exec = app.db.Column(app.db.DATE, nullable=False)
    date_created = app.db.Column(app.db.DATETIME, nullable=False)
    period = app.db.Column(app.db.INTEGER, nullable=False)
    description = app.db.Column(app.db.VARBINARY(1024), nullable=True)
    account_id = app.db.Column(app.db.Integer, app.db.ForeignKey('accounts.id'), nullable=False)
    account_foreign_id = app.db.Column(app.db.Integer, app.db.ForeignKey('accounts.id'), nullable=True)
    amount = app.db.Column(app.db.VARBINARY(128), nullable=False)
    category_id = app.db.Column(app.db.Integer, app.db.ForeignKey('categories.id'), nullable=True)
    contact_id = app.db.Column(app.db.Integer, app.db.ForeignKey('contacts.id'), nullable=True)
    notes = app.db.Column(app.db.VARBINARY, nullable=True)


class Transactions(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    date_valuta = app.db.Column(app.db.DATE, nullable=False)
    date_created = app.db.Column(app.db.DATETIME, nullable=False)
    description = app.db.Column(app.db.VARBINARY(1024), nullable=True)
    account_id = app.db.Column(app.db.Integer, app.db.ForeignKey('accounts.id'), nullable=False)
    account_foreign_id = app.db.Column(app.db.Integer, app.db.ForeignKey('accounts.id'), nullable=True)
    amount = app.db.Column(app.db.VARBINARY(128), nullable=False)
    category_id = app.db.Column(app.db.Integer, app.db.ForeignKey('categories.id'), nullable=True)
    contact_id = app.db.Column(app.db.Integer, app.db.ForeignKey('contacts.id'), nullable=True)
    reoccuring_base = app.db.Column(app.db.Integer, nullable=True)


class Contacts(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    user_id = app.db.Column(app.db.Integer, app.db.ForeignKey('users.id'), nullable=False)
    name = app.db.Column(app.db.VARBINARY(256), nullable=False)


class Categories(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    user_id = app.db.Column(app.db.Integer, app.db.ForeignKey('users.id'), nullable=False)
    name = app.db.Column(app.db.VARBINARY(25), nullable=False)
