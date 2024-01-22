from . import users




@users.route("/")
def list():
    return "User List"