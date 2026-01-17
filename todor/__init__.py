from flask import Flask

def create_app():
    app = Flask(__name__)

    from .todo import todo
    from .auth import auth

    app.register_blueprint(todo)
    app.register_blueprint(auth)

    return app
