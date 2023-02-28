from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import subprocess

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index() -> str:
    return render_template('iRoombaInterface.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('start_program')
def handle_start_program():
    # Start the program here
    subprocess.Popen(['python', '/path/to/iroomba.py'])

if __name__ == '__main__':
    socketio.run(app)
