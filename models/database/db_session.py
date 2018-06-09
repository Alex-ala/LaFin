from app import db


def get_db_session():
    return db.create_scoped_session()
