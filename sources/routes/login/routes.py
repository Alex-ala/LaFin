from flask import Blueprint, render_template
blueprint = Blueprint(
    'login',
    __name__,
    url_prefix='/',
    template_folder='/templates',
    static_folder='/ressources'
)
@blueprint.route('/')
def entry_point():
    return 'LOGIN LOGIN'