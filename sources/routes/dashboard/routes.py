from flask import Blueprint, render_template
blueprint = Blueprint(
    'dashboard',
    __name__,
    url_prefix='/dashboard',
    template_folder='/templates/',
    static_folder='static'
)

@blueprint.route('/')
def entry_point():
    return render_template("dashboard/index.html")
