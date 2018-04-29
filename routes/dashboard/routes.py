from flask import Blueprint, render_template, request, redirect
from models.database import session, dashboard

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
        current_session = session.get_session(request.cookies.get('lafin_session'))
        userid = current_session.user_id
    else:
        return redirect('/user/login')
    return render_template("dashboard/index.html", widgets=dashboard.get_widgets(userid))
