from models.db_schema import *

def get_widgets(userid):
    return Dashboards.query.filter_by(user_id=userid).first().widgets

