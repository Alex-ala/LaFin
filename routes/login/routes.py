from flask import Blueprint, render_template, request, redirect, make_response
# Remove the following imports, replace with models.database logic
from models import database

blueprint = Blueprint(
    'login',
    __name__,
    url_prefix='/login',
    template_folder='/templates',
    static_folder='static'
)


@blueprint.route('/', methods=['GET'])
def login():
    database.clear_sessions()
    return render_template("login/login.html")


@blueprint.route('/', methods=['POST'])
def check_login():
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    validated = database.check_login(username, password)
    if validated:
        token = database.start_session(validated)
        response = make_response(redirect("dashboard/"))
        response.set_cookie('lafin_session', token)
        return response
    else:
        return render_template("login/login.html", login_error=True)
