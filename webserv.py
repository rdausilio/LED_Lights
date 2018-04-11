"""
Rowan D'Ausilio
LED Lightstrip project
"""

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/red')
def red():
    return jsonify(237, 28, 28)


@app.route('/orange')
def orange():
    return jsonify(255, 126, 28)


@app.route('/yellow')
def yellow():
    return jsonify(255, 228, 28)


@app.route('/green')
def green():
    return jsonify(42, 178, 37)


@app.route('/blue')
def blue():
    return jsonify(24, 86, 178)


@app.route('/violet')
def violet():
    return jsonify(128, 18, 165)


@app.route('/custom')
def custom():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
