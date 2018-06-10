import models.widgets
from models.decorators import check_session
from models.database.finance.currentBalance import get_balances_for_user
from flask import render_template

blueprint = models.widgets.blueprints["balanceWidget"]


@blueprint.route('/')
@check_session
def show_balance(user, key):
    return render_template('balance.html', balances=get_balances_for_user(user, key))
