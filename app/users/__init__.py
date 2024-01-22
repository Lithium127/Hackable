from flask import Blueprint

users = Blueprint("users", __name__, url_prefix="/user", template_folder="templates")

from . import views