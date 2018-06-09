#!/usr/bin/python
# coding: utf-8
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from models.dbconfig import connect_string
import widgets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = connect_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def register_blueprints(app):
    for module_name in ('routes.dashboard', 'routes.login', 'routes.debug'):
        module = import_module('{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/site-map")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(url)
    return '<br>'.join(links)


widgets.load(app)
register_blueprints(app)
if __name__ == '__main__':
    app.run(debug=True)
