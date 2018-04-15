from flask import Blueprint, render_template
blueprint = Blueprint(
    'login_blueprint',
    __name__,
    url_prefix='/login',
    template_folder='/templates',
    static_folder='/ressources'
)

@blueprint.route('/')
def entry_point():
    return 'Hello World2!'