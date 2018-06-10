import secrets
from models.db_schema import *
from models.database.db_session import get_db_session
import app

def start_session(userid):
    db = get_db_session()
    session_token = secrets.token_hex(64)
    csrf_token = secrets.token_hex(64)
    session = Sessions(session_token=session_token, csrf_token=csrf_token, user_id=userid)
    db.add(session)
    db.commit()
    return session_token


def stop_session(token):
    db = app.db.session
    session = Sessions.query.filter_by(session_token=token).first()
    db.delete(session)
    db.commit()


def clear_sessions():
    db = app.db.session
    sessions = Sessions.query.all()
    for session in sessions:
        expire = session.created + datetime.timedelta(minutes=15)
        if expire < datetime.datetime.now():
            db.delete(session)
    db.commit()


def get_session(token):
    return Sessions.query.filter_by(session_token=token).first()


def update_session(token):
    session = Sessions.query.filter_by(session_token=token).first()
    session.created = datetime.datetime.now()
    clear_sessions()
