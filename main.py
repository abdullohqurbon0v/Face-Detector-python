import cv2

def blur_face(img):
    (h, w) = img.shape[:2]
    dW = max(1, (w // 3) | 1)
    dH = max(1, (h // 3) | 1)
    return cv2.GaussianBlur(img, (dW, dH), 0)

capture = cv2.VideoCapture(0)
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, img = capture.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, scaleFactor=2, minNeighbors=5, minSize=(20, 20))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        img[y:y+h, x:x+w] = blur_face(img[y:y+h, x:x+w])

    cv2.imshow('From camera', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()
