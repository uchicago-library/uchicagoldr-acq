from flask import Flask
from app.acq.views import acquistions

app = Flask(__name__)
app.register_blueprint(acquistions)
app.run()
