import eventlet
import socketio
import cv2
import pickle


sio = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(sio)


@sio.event
def server(sid, frame):
    data = pickle.loads(frame)
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)

    cv2.imshow("Video", data)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        exit(0)


if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(("", 8000)), app)
