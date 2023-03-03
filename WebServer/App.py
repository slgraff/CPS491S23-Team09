from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import socketio
import subprocess

sio = socketio.Server() #creating socketio server instance 


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index() -> str:
    return render_template('iRoombaInterface.html')

@socketio.on('connect') #event handler when client connects to server the connect function is called and logs message to console.
def connect(sid, environ):
    print('Client connected', sid)

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')


@socketio.on('start_program') #when event is emiited from web interface this function is called which start tetheredDrive.py using the subporcess module
def start_program(sid):
    print('Starting TetheredDrive.py')

    import os # possiblyremove later 
    directory = "logs" # possiblyremove later 

    # create logs directory if does not exist
    if not os.path.exists(directory):# possiblyremove later 
        os.makedirs(directory) # possiblyremove later 
    # Start the program here
    subprocess.Popen(['python', '/workspaces/CPS491S23-Team09/Create2/TetheredDrive'])

app = socketio.WSGIApp(sio)

if __name__ == '__main__':
    #socketio.run(app) possibly remove switch to lower line 
    app.run()
