from flask import Blueprint, render_template, request, redirect
from models.database import session, dashboard
from models.decorators import check_session

blueprint = Blueprint(
    'dashboard',
    __name__,
    url_prefix='/dashboard',
    template_folder='/templates/',
    static_folder='static'
)


@blueprint.route('/')
@check_session
def entry_point(userid, key):
    return render_template("dashboard/index.html", widgets=dashboard.get_widgets(userid))

#TODO: Route for each account (/dashboard/1) -> Show transactions only for this account
#TODO: ImportWidget uses dashboards accountid if none given
#TODO: WidgetSettings for TransactionsWidget