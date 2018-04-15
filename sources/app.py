#!/usr/bin/python
# coding: utf-8
from flask import Flask
from importlib import import_module

app = Flask(__name__)

def register_blueprints(app):
    for module_name in ('routes.dashboard', 'routes.login'):
        module = import_module('{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

register_blueprints(app)
if __name__ == '__main__':
    app.run(debug=True)
