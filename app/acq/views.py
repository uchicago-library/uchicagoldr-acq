from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

acquistions = Blueprint('simple_page', __name__, template_folder="templates")

@acquistions.route('/')
def front():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

