from flask import Blueprint, render_template
# Remove the following imports, replace with models.database logic
from models import db_schema
from app import db

blueprint = Blueprint(
    'login',
    __name__,
    url_prefix='/login',
    template_folder='/templates',
    static_folder='/ressources'
)
@blueprint.route('/')
def entry_point():
    #Replace with models.database logic
    user = db_schema.Users(name="hop",email="hop@hop",password="keks",salt="1234")
    db.session.add(user)
    db.session.commit()
    return render_template("login/login.html")
