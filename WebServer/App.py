from flask import Flask, render_template
from flask_socketio import SocketIO
import subprocess
import os

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index() -> str:
    return render_template('iRoombaInterface.html')


# event handler when client connects to server the connect function is called and logs message to console.
@socketio.on('connect')
def connect(sid):
    """
    Event Handler called when client connects to the server. 
    :param sid: The session ID for client 
    """
    print('Client connected', sid)


@socketio.on('disconnect')
def disconnect():
    """
    Event handler called when a client disconnects from the server.
    """
    print('Client disconnected')


# when event is emitted from web interface this function is called which start tetheredDrive.py using the subporcess module
@socketio.on('start_program')
def start_program():
    """
    Event handler called when the 'start_program' event is emitted from the web interface.
    Starts the TetheredDrive.py program using the subprocess module.
    """
    print('Starting TetheredDrive.py')

    directory = "logs"  # possiblyremove later

    # create logs directory if does not exist
    if not os.path.exists(directory):  # possiblyremove later
        os.makedirs(directory)  # possiblyremove later
    # Start the program here
    subprocess.Popen(
        ['python', '/workspaces/CPS491S23-Team09/Create2/TetheredDrive.py'])


if __name__ == '__main__':
    socketio.init_app(app)  # possibly remove switch to lower line
    app.run()
    
