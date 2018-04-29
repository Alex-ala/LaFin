from flask import Blueprint, render_template, request, redirect, make_response
# Remove the following imports, replace with models.database logic
from models.database import user, session

blueprint = Blueprint(
    'login',
    __name__,
    url_prefix='/user',
    template_folder='/templates',
    static_folder='static'
)


@blueprint.route('/login', methods=['GET'])
def login():
    session.clear_sessions()
    return render_template("login/login.html")


@blueprint.route('/login', methods=['POST'])
def check_login():
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    token = user.check_login(username, password)
    if token is None:
        return render_template("login/login.html", login_error=True)
    else:
        response = make_response(redirect("dashboard/"))
        response.set_cookie('lafin_session', token)
        return response


@blueprint.route('/logout')
def logout():
    token = request.cookies.get('lafin_session')
    if token is None:
        return redirect('/user/login')
    response = make_response(redirect('/user/login'))
    response.set_cookie('lafin_session', '', expires=0)
    user.logout(token)
    return response
