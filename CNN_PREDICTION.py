from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
#------------------------------
# sess = tf.Session()
# keras.backend.set_session(sess)
#------------------------------

#------------------------------
import os, cv2, keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.engine.saving import load_model
# manipulate with numpy,load with panda
import numpy as np
# import pandas as pd

# data visualization
import cv2
my_list = os.listdir(r'C:\Users\SREERAG\PycharmProjects\scd\src\static\Dataset')
print(my_list)
# Data Import
def read_dataset():
    data_list = []
    label_list = []
    i=-1
    my_list = os.listdir(r'C:\Users\00000\Downloads\scd (2)\scd\src\static\dataset')
    for pa in my_list:
        i=i+1
        if(i==10):
            break
        print(pa,"==================",i)
        for root, dirs, files in os.walk(r'C:\Users\00000\Downloads\scd (2)\scd\src\static\dataset\\' + pa):

         for f in files:
            file_path = os.path.join(r'C:\Users\00000\Downloads\scd (2)\scd\src\static\dataset\\'+pa, f)
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
            data_list.append(res)

            label = i
            label_list.append(label)
            # label_list.remove("./training")
    return (np.asarray(data_list, dtype=np.float32), np.asarray(label_list))

def read_dataset1(path):
    data_list = []
    label_list = []

    file_path = os.path.join(path)
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
    data_list.append(res)
    # label = dirPath.split('/')[-1]

            # label_list.remove("./training")
    return (np.asarray(data_list, dtype=np.float32))

def predict(fn):
    dataset=read_dataset1(fn)
    (mnist_row, mnist_col, mnist_color) = 48, 48, 1
    dataset = dataset.reshape(dataset.shape[0], mnist_row, mnist_col, mnist_color)
    dataset = dataset/255
    mo = load_model(r"C:\Users\SREERAG\PycharmProjects\scd\src\model1.h5")
    # predict probabilities for test set
    yhat_classes = mo.predict_classes(dataset, verbose=0)
    return yhat_classes
