from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

acquistions = Blueprint('simple_page', __name__, template_folder="templates")


@acquistions.route('/')
def front():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@acquistions.route("/list")
def list_records():
    try:
        return render_template('list.html')
    except TemplateNotFound:
        abort(404)


@acquistions.route("/record")
def record():
    try:
        return render_template("record.html")
    except TemplateNotFound:
        abort(404)
