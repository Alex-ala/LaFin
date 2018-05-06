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
    tokenkey = user.check_login(username, password)
    if tokenkey is None:
        return render_template("login/login.html", login_error=True)
    else:
        response = make_response(redirect("dashboard/"))
        print(tokenkey)
        response.set_cookie('lafin_session', tokenkey[0], max_age=900)
        response.set_cookie('lafin_key', tokenkey[1], max_age=900)
        return response


@blueprint.route('/logout')
def logout():
    token = request.cookies.get('lafin_session')
    if token is None:
        return redirect('/user/login')
    response = make_response(redirect('/user/login'))
    response.set_cookie('lafin_session', '', max_age=0)
    response.set_cookie('lafin_key', '', max_age=0)
    user.logout(token)
    return response
