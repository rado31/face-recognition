import face_recognition
import cv2
import numpy as np
import pickle
import socketio
import requests


sio = socketio.Client()
sio.connect("http://127.0.0.1:8000")

is_running = True

video_capture = cv2.VideoCapture(0)


@sio.event
def stop():
    global is_running
    is_running = False


rado_image = face_recognition.load_image_file("rado.jpg")
rado_face_encoding = face_recognition.face_encodings(rado_image)[0]

aygul_image = face_recognition.load_image_file("Aygul.jpeg")
aygul_face_encoding = face_recognition.face_encodings(aygul_image)[0]

bahar_image = face_recognition.load_image_file("Bahargul.jpeg")
bahar_face_encoding = face_recognition.face_encodings(bahar_image)[0]

meylis_image = face_recognition.load_image_file("Meylis.jpeg")
meylis_face_encoding = face_recognition.face_encodings(meylis_image)[0]

gunca_image = face_recognition.load_image_file("Guncha.jpeg")
gunca_face_encoding = face_recognition.face_encodings(gunca_image)[0]

known_face_encodings = [
    rado_face_encoding,
    aygul_face_encoding,
    bahar_face_encoding,
    meylis_face_encoding,
    gunca_face_encoding,
]
known_face_names = [
    "rado",
    "Aygul Halmyradowa",
    "Bahargul Ankarowa",
    "Meylis Syhyyew",
    "Gunca Yaylimowa",
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
ids = []

while is_running:
    ret, frame = video_capture.read()

    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding
            )
            name = ""

            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding
            )

            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]

                if best_match_index not in ids:
                    ids.append(best_match_index)
                    requests.get(f"http://127.0.0.1/user/{best_match_index}")

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        if name != "":
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            cv2.rectangle(
                frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED
            )
        else:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(
                frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED
            )

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    ret, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 30])
    x_as_bytes = pickle.dumps(buffer)
    sio.emit("server", x_as_bytes)

video_capture.release()
