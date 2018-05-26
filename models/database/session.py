import secrets
from models.db_schema import *


def start_session(userid):
    session_token = secrets.token_hex(64)
    csrf_token = secrets.token_hex(64)
    session = Sessions(session_token=session_token, csrf_token=csrf_token, user_id=userid)
    db.session.add(session)
    db.session.commit()
    return session_token


def stop_session(token):
    session = Sessions.query.filter_by(session_token=token).first()
    db.session.delete(session)
    db.session.commit()


def clear_sessions():
    sessions = Sessions.query.all()
    for session in sessions:
        expire = session.created + datetime.timedelta(minutes=15)
        if expire < datetime.datetime.now():
            db.session.delete(session)
    db.session.commit()


def get_session(token):
    return Sessions.query.filter_by(session_token=token).first()


def update_session(token):
    session = Sessions.query.filter_by(session_token=token).first()
    session.created = datetime.datetime.now()
    clear_sessions()
