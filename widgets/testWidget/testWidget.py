import models.widgets
from models.database.user import decrypt
from models.db_schema import Transactions
from models.decorators import check_session
blueprint = models.widgets.blueprints["testWidget"]

@blueprint.route('/')
@check_session
def entry_point(userid, key):
    trans = Transactions.query.filter_by(account_id=1)
    res = ""
    for t in trans:
        res += decrypt(t.description, key).decode('utf-8') + "<br/>"
    return res
