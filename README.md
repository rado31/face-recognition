# Need to add your image, for detection

This project works by p2p connection with socket. Client sending the frames of a camera to the server.
Then server shows the live camera.

- create a virtual environment:
  ```bash
  python -m venv venv # or python3 on linux and mac
  ```
- activate venv
  ```bash
  source venv/bin/activate # on linux and mac
  .\venv\Scripts\activate # on fu***g windows -_-
  ```
- install dependencies
  ```bash
  pip install -r requirements.txt
  ```
- Make a selfie
- move the image to the root project (near the client and server files)
- update a code below (or add another, if you have several bitches)

```python
rado_image = face_recognition.load_image_file("rado.jpg")
rado_face_encoding = face_recognition.face_encodings(rado_image)[0]

known_face_encodings = [
    rado_face_encoding,
]
known_face_names = [
    "rado"
]
```
- Update the hosts and ports if you need
- Run server and client on separate terminals

## I hope you've got it -_- (if you don't, it's your problem)
