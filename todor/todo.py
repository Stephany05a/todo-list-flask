from flask import Blueprint, jsonify

todo = Blueprint("todo", __name__)

@todo.route("/")
def index():
    return jsonify({
        "mensaje": "Todo List funcionando correctamente"
    })
