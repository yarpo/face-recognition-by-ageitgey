import face_recognition

def load_file_from_folder(folder, name):
    path = f'./img/{folder}/{name}.jpg'
    image = face_recognition.load_image_file(path)
    return face_recognition.face_encodings(image)[0]

def load_known(name):
    return load_file_from_folder('known', name)

def load_unknown(name):
    return load_file_from_folder('unknown', name)

def is_the_same_person(image_encoding1, image_encoding2):
    return face_recognition.compare_faces([image_encoding1], image_encoding2)[0]

def compare_faces(known_person, unknown_person):
    known_face = load_known(known_person)
    unknown_face = load_unknown(unknown_person)

    if is_the_same_person(known_face, unknown_face):
        print(f'This is {known_person}')
    else:
        print(f'This is NOT {known_person}')

compare_faces('Patryk Jar', 'obama')