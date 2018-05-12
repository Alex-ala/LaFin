from flask import request, Blueprint
from models.database.user import encrypt, decrypt, add_user
from app import app

blueprint = Blueprint(
    'debug',
    __name__,
    url_prefix='/debug',
    template_folder='/',
    static_folder='static'
)

@blueprint.route('/testEncryption')
def test_encryption():
    data = request.args.get('data').encode('utf-8')
    key = request.cookies.get('lafin_key')
    return encrypt(data, key)

@blueprint.route('/testDecryption')
def test_decryption():
    data = request.args.get('data').encode('utf-8')
    key = request.cookies.get('lafin_key')
    return decrypt(data, key)

@blueprint.route('/createAccount')
def create_account():
    add_user('a@b.c', 'a@b.c', 'a@b.c')
    return "User a@b.c created"
