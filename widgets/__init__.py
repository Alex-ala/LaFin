from flask import Blueprint
from importlib import import_module
from models.widgets import add_widget
import pkgutil
from sys import modules

def load(app):
    currentPath = modules[__name__].__path__
    for importer, module_name, ispkg in pkgutil.iter_modules(currentPath):
        blueprint = Blueprint(
            module_name,
            __name__,
            url_prefix='/widgets/'+module_name,
            template_folder='templates',
            static_folder='ressources'
        )
        add_widget(module_name, blueprint)
        import_module('widgets.'+module_name+"."+module_name)
        app.register_blueprint(blueprint)
        print("Registered widget "+module_name)
