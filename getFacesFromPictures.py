from os import walk
import face_recognition
from PIL import Image
import cv2

f = []
i = 0
for (dirpath, dirnames, filenames) in walk("downloads/sad person"):
    for filename in filenames:
        try:
            image = face_recognition.load_image_file("downloads/sad person/" + filename)

        except:
            continue

        face_locations = face_recognition.face_locations(image)

        im = Image.open("downloads/sad person/" + filename)
        k = 0
        i += 1
        for face_location in face_locations:
            k += 1
            face_location_parsed= (face_location[3],face_location[0], face_location[1], face_location[2])
            imCropped = im.crop(face_location_parsed)
            str = "sadData/{}_{}.png".format(i,k)
            imCropped.save(str)

    break