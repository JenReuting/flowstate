import os
from flask import Flask
from dotenv import load_dotenv
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ['DATABASE_URL'].replace("postgres://", "postgresql://"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

connect_db(app)

# toolbar = DebugToolbarExtension(app)

####################################################################








##############################################################################
# Turn off all caching in development

@app.after_request
def add_header(response):
    """Add non-caching headers on every response."""
    response.cache_control.no_cache = True
    return response