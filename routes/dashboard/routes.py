from flask import Blueprint, render_template, request, redirect
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
    if 'lafin_session' in request.cookies:
        session = database.get_session(request.cookies.get('lafin_session'))
        userid = session.user_id
    else:
        return redirect('/login')
    return render_template("dashboard/index.html", widgets=database.get_widgets(userid))
