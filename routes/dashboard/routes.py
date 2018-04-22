from flask import Blueprint, render_template, session
from models import database

blueprint = Blueprint(
    'dashboard',
    __name__,
    url_prefix='/dashboard',
    template_folder='/templates/',
    static_folder='static'
)

@blueprint.route('/')
def entry_point():
    userid = 1
    return render_template("dashboard/index.html", widgets=database.getWidgets(userid))
