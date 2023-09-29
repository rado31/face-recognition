import eventlet
import socketio
import cv2
import pickle
from sys import exit


sio = socketio.Server()
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
def server(sid, frame):
    data = pickle.loads(frame)
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)

    cv2.imshow('Video', data)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        sio.emit('stop')
        exit(0)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
