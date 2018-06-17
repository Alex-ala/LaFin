from models.database.session import get_session, update_session
from models.database.user import check_account_permissions
from flask import request, redirect, abort
from functools import wraps

def check_session(f):
    @wraps(f)
    def check(*args, **kws):
        cookies = request.cookies
        if not ('lafin_session' in cookies and 'lafin_key' in cookies):
            return redirect('/user/login')
        current_session = get_session(cookies.get('lafin_session'))
        if current_session is None:
            return redirect('/user/login')
        update_session(cookies.get('lafin_session'))
        userid = current_session.user_id
        key = cookies.get('lafin_key')
        if 'account_id' in kws:
            if check_account_permissions(userid, kws["account_id"]):
                return f(userid,key,kws["account_id"])
            else:
                return abort(403)
        else:
            return f(userid, key)
    return check
