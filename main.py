import cv2
import face_recognition
import os
import numpy as np


# 1. Load known faces

known_encodings = []
known_names = []

folder = "images"

for image_name in os.listdir(folder):

    image_path = os.path.join(folder, image_name)

    # Only process image files
    if not image_name.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    print("Loading:", image_name)

    try:

        # Load image
        image = face_recognition.load_image_file(image_path)

        # Convert to uint8
        image = np.asarray(image, dtype=np.uint8)

        # Make image contiguous
        image = np.ascontiguousarray(image)

        print("Image dtype:", image.dtype)
        print("Image shape:", image.shape)

        # Find face encoding
        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:

            # Store encoding
            known_encodings.append(encodings[0])

            # Get name from filename
            name = os.path.splitext(image_name)[0]

            # Remove numbers from name
            name = name.rstrip("0123456789")

            known_names.append(name)

        else:
            print("No face found in:", image_name)

    except Exception as e:

        print("Error in image:", image_name)
        print(e)


print()
print("Known people:")
print(known_names)


# 2. Open webcam


vid = cv2.VideoCapture(0)

if not vid.isOpened():

    print("Error: Could not open webcam.")
    exit()


while True:

    ret, frame = vid.read()

    if not ret:

        print("Failed to read webcam.")
        break


    # Mirror webcam
    frame = cv2.flip(frame, 1)


    
    # 3. BGR → RGB
    

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # 4. Fix image type
   

    rgb_frame = np.asarray(
        rgb_frame,
        dtype=np.uint8
    )

    rgb_frame = np.ascontiguousarray(
        rgb_frame
    )


    # 5. Detect faces


    face_locations = face_recognition.face_locations(
        rgb_frame
    )


    # 6. Get face encodings
   

    face_encodings = face_recognition.face_encodings(
        rgb_frame,
        face_locations
    )


  
    # 7. Recognize each face


    for face_encoding, face_location in zip(
        face_encodings,
        face_locations
    ):

        matches = face_recognition.compare_faces(
            known_encodings,
            face_encoding
        )

        name = "Unknown"


        for i in range(len(matches)):

            if matches[i]:

                name = known_names[i]

                break


        # 8. Bounding box
        

        top, right, bottom, left = face_location


    
        # 9. Draw rectangle
      

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0, 255, 0),
            2
        )


    
        # 10. Display name


        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    # 11. Display webcam
  

    cv2.imshow(
        "Face Recognition",
        frame
    )


    # Press M to exit
    if cv2.waitKey(1) & 0xFF == ord("m"):

        break


# 12. Cleanup

vid.release()

cv2.destroyAllWindows()

