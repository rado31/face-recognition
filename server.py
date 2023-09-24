import cv2
import socket
import pickle


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8000))

while True:
    x = s.recvfrom(1000000)
    data = x[0]
    data = pickle.loads(data)
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)

    cv2.imshow('Video', data)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
