"""
Openshow: media presentation application
"""
from flask import Flask, send_from_directory, send_file
# from flask_socketio import SocketIO, Namespace, emit


app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)


@app.route('/bower_components/<path:path>')
def send_bower_components(path):
    return send_from_directory('bower_components', path)


@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)


@app.route('/src/<path:path>')
def send_src(path):
    return send_from_directory('src', path)


@app.route('/service-worker.js')
def service_worker():
    return send_file('service-worker.js')


@app.route('/')
def index():
    return send_file('index.html')


if __name__ == '__main__':
    app.run()
