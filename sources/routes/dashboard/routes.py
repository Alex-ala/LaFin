from flask import Blueprint, render_template
blueprint = Blueprint(
    'dashboard_blueprint',
    __name__,
    url_prefix='/',
    template_folder='/templates',
    static_folder='/ressources'
)

@blueprint.route('/')
def entry_point():
    return 'Hello World!'