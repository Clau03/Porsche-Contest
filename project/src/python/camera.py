
# import cv2
# import numpy as np
# import tensorflow as tf
# import os
# import time

# # Load pre-trained model
# model = tf.saved_model.load("/home/rpy")#('/home/rpy/model_data.bin')


# capture_duration = 1  # capture images for 5 seconds
# image_folder = '/home/rpy/images1'  # folder to save captured images

# # initialize the camera and set the resolution
# camera = cv2.VideoCapture(0)
# camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# # create the folder if it doesn't exist
# os.makedirs(image_folder, exist_ok=True)

# # start capturing images
# start_time = time.time()
# count = 0  # keep track of the number of captured images
# while time.time() - start_time < capture_duration:
#     ret, frame = camera.read()   # read a frame from the camera
#     if ret:                      # check if the frame was captured successfully
#         # resize the image to 320x240 pixels
#         frame = cv2.resize(frame, (320, 240))
#         # save the image as PNG file
#         image_filename = os.path.join(image_folder, f'image_{count:04d}.png')
#         cv2.imwrite(image_filename, frame)
#         count += 1
#     else:
#         break

# # stop capturing and release resources
# camera.release()
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
# import tensorflow as tf
# import os
# import time

# # Load pre-trained model
# model = tf.keras.models.load_model("/home/rpy/saved_model.pb")

# capture_duration = 5  # capture images for 5 seconds
# image_folder = '/home/rpy/images1'  # folder to save captured images
# result_file = '/home/rpy/result.txt'  # file to save the inference results

# # initialize the camera and set the resolution
# camera = cv2.VideoCapture(0)
# camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# # create the folder if it doesn't exist
# os.makedirs(image_folder, exist_ok=True)

# # start capturing images
# start_time = time.time()
# count = 0  # keep track of the number of captured images
# images = []  # list to hold the captured images
# while time.time() - start_time < capture_duration:
#     ret, frame = camera.read()   # read a frame from the camera
#     if ret:                      # check if the frame was captured successfully
#         # resize the image to 320x240 pixels
#         frame = cv2.resize(frame, (30, 30))
#         # save the image as PNG file
#         image_filename = os.path.join(image_folder, f'image_{count:04d}.png')
#         cv2.imwrite(image_filename, frame)
#         # add the image to the list
#         images.append(frame)
#         count += 1
#     else:
#         break

# # stop capturing and release resources
# camera.release()

# # convert the list of images to a numpy array
# images = np.array(images)

# # feed the images to the model for inference
# predictions = model(images)

# # save the inference results to a file
# with open(result_file, 'w') as f:
#     for i, pred in enumerate(predictions):
#         f.write(f'Image {i}: {pred}\n')
        




import cv2
import numpy as np
import tensorflow as tf
import os
import subprocess

# Load pre-trained model
model = tf.keras.models.load_model("C:\\Users\\claus\\Downloads\\project\\src\\python\\my_model.h5")

capture_duration = 5  # capture images for 5 seconds
image_folder = '/home/rpy/images1'  # folder to save captured images
result_file = '/home/rpy/result.txt'  # file to save the inference results

# initialize the camera and set the resolution
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# create the folder if it doesn't exist
os.makedirs(image_folder, exist_ok=True)

# start capturing images
start_time = time.time()
count = 0  # keep track of the number of captured images
images = []  # list to hold the captured images
while time.time() - start_time < capture_duration:
    ret, frame = camera.read()   # read a frame from the camera
    if ret:                      # check if the frame was captured successfully
        # resize the image to 320x240 pixels
        frame = cv2.resize(frame, (30, 30))
        # save the image as PNG file
        image_filename = os.path.join(image_folder, f'image_{count:04d}.png')
        cv2.imwrite(image_filename, frame)
        # add the image to the list
        images.append(frame)
        count += 1
    else:
        break

# stop capturing and release resources
camera.release()

# convert the list of images to a numpy array
images = np.array(images)

# feed the images to the model for inference
predictions = model(images)

# save the inference results to a file
with open(result_file, 'w') as f:
    for i, pred in enumerate(predictions):
        f.write(f'Image {i}: {pred}\n')

# call the C++ program to transfer the results to the server
transfer_result = subprocess.run(["./transfer", result_file], capture_output=True)

# check the return code and print any output or error messages
if transfer_result.returncode == 0:
    print("Results transferred successfully")
    print(transfer_result.stdout.decode('utf-8'))
else:
    print("Results transfer failed with return code:", transfer_result.returncode)
    print(transfer_result.stderr.decode('utf-8'))