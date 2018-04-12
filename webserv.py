"""
Rowan D'Ausilio
LED Lightstrip project
"""

from flask import Flask, render_template, jsonify
from pick_color import Color_Picker

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/red')
def red():
    return jsonify(237, 28, 28, 0)


@app.route('/orange')
def orange():
    return jsonify(255, 126, 28, 0)


@app.route('/yellow')
def yellow():
    return jsonify(255, 228, 28, 0)


@app.route('/green')
def green():
    return jsonify(42, 178, 37, 0)


@app.route('/blue')
def blue():
    return jsonify(24, 86, 178, 0)


@app.route('/purple')
def purple():
    return jsonify(128, 18, 165, 0)


@app.route('/custom')
def custom():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
