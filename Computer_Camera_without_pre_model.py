#import threading
import cv2
import keras
import tensorflow as tf
import mediapipe as mp
import numpy as np
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time



global label


global IMAGE_HEIGHT
global IMAGE_SIZE

global original_size
global counterNV
global counterV
global frame_original
def draw_class_on_image(label, frame):  # Draw the label on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 30)
    fontScale = 1
    if label == "Violence":
        fontColor = (0, 0, 255)  # Red
    else:
        fontColor = (0, 255, 0)  # green
    thickness = 2
    lineType = 2
    cv2.putText(frame, str(label),
                bottomLeftCornerOfText,
                font,
                fontScale,
                fontColor,
                thickness,
                lineType)
    return frame


def detect(model, frames):  # Classifies the frames by the model and return the label
    predicted_labels_probabilities = np.zeros(shape=(1, 2))
    predicted_labels_probabilities = model.predict(frames)
    print('#################################')
    print(predicted_labels_probabilities)
    if predicted_labels_probabilities[0][0] > 0.5:
        label = "Violence"
    else:
        label = "Non Violence"

    return label

def main(video):
    label = "Non Violence"  # Default label

    cap = cv2.VideoCapture(video)  # לפתוח מצלמה-0 או לשים סרטונים

    model = keras.models.load_model("cnn_lstm_model_PRO.hdf5")  # load our model from Colab
    print(model.input_shape)  # The number of dimensions in the matrix (None, 10, 224, 224, 3)

    # i = 0
    # warm_up_frames = 2
    IMAGE_SIZE = 64
    resized_frames = np.zeros(shape=(1, 10, IMAGE_SIZE, IMAGE_SIZE, 3),
                              dtype=np.float32)  # float32 to minimze using RAM
    frames = np.zeros(shape=(10, IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.float32)  # float32 to minimze using RAM

    counterV = 0
    counterNV = 0

    while True:
        frames_list = []
        # for j in range(10):# השאלה אם לעשות את הלולאה עבור כל 10 פריימים שונים או לקחת פריים אחד ולהכניס אותו 10 פעמים לתוך רשימה
        # ret == false - there is error
        for j in range(10):
            ret, frame = cap.read()
            if ret == True:
                frame_original = cv2.resize(frame, (500, 500))
                frame = cv2.resize(frame, (IMAGE_SIZE, IMAGE_SIZE))  # Adjusts the frame to the size the model knows
                frame = frame / 255
                # time.sleep(0.04)
                # time.sleep(0.04)   תשימו לב שאם שולחים סרטון אז זה מאט את הקצב כי הסרטון רץ מהר!ואם עושים ממצלמה לא צריך את זה
                frames_list.append(frame)
            else:
                break

        if len(frames_list) < 10:
            # print("Final:"+ max(counterV,counterNV))
            break
        frames = np.array(frames_list).reshape(1, 10, IMAGE_SIZE, IMAGE_SIZE, 3)
        # i = i + 1
        print('Took 10 Frames Successfully')
        resized_frames[0][:] = frames
        print(resized_frames.shape)
        # לא ברור אם נצטרך להשתמש בזה כרגע זה עבד גם בלי זה..if i > warm_up_frames:
        print("Start detecting...")
        # t1 = threading.Thread(target=detect, args=(model, resized_frames))  # Threads
        # t1.start()
        label = detect(model, resized_frames)
        if label == "Violence":
            counterV = counterV + 1
        else:
            counterNV = counterNV + 1
        print("!!!!!!!!!!!!!!!!!!!")
        print(label)
        # print(t1)
        frame_original = draw_class_on_image(label, frame_original)
        # frame = draw_class_on_image(label, frame)
        cv2.imshow("image", frame_original)

        if cv2.waitKey(1) == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()


    if counterNV > counterV:
        #print("Non Violence")
        return "Non Violence"
    if counterNV < counterV:
        #print("Violence")
        return "Violence"
    if counterNV == counterV:
        #print("counterNV = counterV")
        return "counterNV = counterV"




