from flask import Flask, render_template, jsonify
import os


app = Flask(__name__, static_folder='static', template_folder='templates')
VERSION = os.getenv('VERSION', '0.1.0')


@app.route('/')
def index():
return render_template('index.html', name='Apple', emoji='🍎', version=VERSION)


@app.route('/health')
def health():
return jsonify(status='ok', service='apple', version=VERSION)


@app.route('/health/live')
def liveness():
return jsonify(status='alive', service='apple')


@app.route('/health/ready')
def readiness():
ready = True # replace with real checks (DB, cache, etc.)
return (jsonify(status='ready', service='apple') if ready
else (jsonify(status='not-ready', service='apple'), 503))


if __name__ == '__main__':
app.run(host='0.0.0.0', port=5001)
