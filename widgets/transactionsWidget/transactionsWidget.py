import models.widgets
from models.database.user import decrypt
from models.db_schema import Transactions
from models.decorators import check_session
blueprint = models.widgets.blueprints["transactionsWidget"]

@blueprint.route('/')
@check_session
def entry_point(userid, key):
    trans = Transactions.query.filter_by(account_id=1)
    res = "<table>"

    for t in trans:
        res += "<tr><td>"+t.date_valuta.strftime("%Y-%m-%d") +\
               "</td><td><b>"+decrypt(t.amount, key).decode('utf-8') +\
               "</b></td><td>"+decrypt(t.description,key).decode('utf-8') + "</tr>"
    return res
