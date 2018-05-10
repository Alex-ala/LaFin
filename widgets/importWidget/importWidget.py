import models.widgets
from flask import render_template
blueprint = models.widgets.blueprints["importWidget"]

@blueprint.route('/')
def entry_point():
    return render_template('import.html')