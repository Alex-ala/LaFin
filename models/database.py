from models.db_schema import *

def getWidgets(userid):
    return Dashboards.query.filter_by(user_id=userid).first().widgets