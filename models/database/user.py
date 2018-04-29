from models.db_schema import *
from models.database.session import *
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64


def check_login(username, password):
    user = Users.query.filter_by(name=username).first()
    if user is None:
        return None
    if user.password == password:
        key = get_encryption_key(password, user.salt)
        token = start_session(user.id)
        encryption_keys.append((key, token))
        return token
    else:
        return False


def logout(session_token):
    if Sessions.query.filter_by(session_token=session_token).first() is None:
        return
    key = [item for item in encryption_keys if item[1] == session_token]
    encryption_keys.remove(key[0])
    stop_session(session_token)


def get_encryption_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))
    return Fernet(key)


def add_user(name, email, password):
    user = Users(name=name, email=email, password=password, salt=secrets.token_bytes(32))
    db.session.add(user)
    db.session.commit()
