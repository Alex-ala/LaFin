from app import db

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),unique=True, nullable=False)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR, nullable=False)
    email = db.Column(db.VARCHAR)
    password = db.Column(db.CHAR, nullable=False)


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
    options = db.Column(db.VARCHAR)


def getWidgets(userid):
    return Dashboards.query.filter_by(user_id=userid).first().widgets