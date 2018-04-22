import models.widgets
blueprint = models.widgets.blueprints["testWidget"]

@blueprint.route('/')
def entry_point():
    return 'IMA TESTWIDGET'