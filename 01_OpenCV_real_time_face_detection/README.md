## :black_heart: Real-Time face recognition (detection) 

You can find all details from [Real-Time Face Recognition: An End-to-End Project (in English)](https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826) and [실시간 얼굴인식 카메라 (in Korean)](https://blog.naver.com/ljy9378/221438230814)
To mount Raspberry camera and set up it, please check my [Raspberry_pi_setup](https://github.com/soyounson/Raspberry_Pi_setup) repository. You can run two python codes `test_photo.py` and `test_video.py` to check your camera. 

### Install OpenCV 4.2.0 on Raspberry Pi :strawberry:
Follow [installation instructions on Github](https://github.com/dltpdn/opencv-for-rpi/releases).
All details in Korean can be found [here](https://github.com/dltpdn/opencv-for-rpi).

open your terminal, update first and download release file
```
pi@raspberrypi: ~ $ sudo apt-get update
pi@raspberrypi: ~ $ wget https://github.com/dltpdn/opencv-for-rpi/releases/download/4.2.0_buster_pi3b/opencv4.2.0.deb.tar
``` 
unzip the file and then install it
```
pi@raspberrypi: ~ $ tar -xvf opencv4.2.0.deb.tar
pi@raspberrypi: ~ $ sudo apt-get install -y ./OpenCV*.deb
``` 

Okay, lets check version of OpenCV
```
pi@raspberrypi: ~ $ pkg-config --modversion opencv4
4.2.0
``` 

or 
```
pi@raspberrypi: ~ $ python
Python 3.7.3 (default, Mar 27 2019, 16:54:48) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> cv2.__version__
'4.2.0'
``` 

### Download Haar Cascade classifier file
For face detection, need `haarcascade_frontalface_default.xml`
 >The most common way to detect a face (or any objects), is using the "Haar Cascade classifier" Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images (ref. [Real-Time Face Recognition: An End-to-End Project (English)](https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826))

```
pi@raspberrypi: ~ $ mkdir fdCam
pi@raspberrypi: ~ $ cd fdCam
pi@raspberrypi: ~ $ wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
```
Then, clone python code from this repository and run it
```
pi@raspberrypi: ~ $ git clone https://github.com/soyounson/Raspberry_Pi_Real-Time_Face_Recognition.git
pi@raspberrypi: ~ $ python faceDetection.py
```
To stop it, press `ESC`

### Dataset :bar_chart:
Make directory to save dataset (photos) and run python code

```
pi@raspberrypi: ~ $ mkdir dataset
pi@raspberrypi: ~ $ python 01_face_dataset.py
enter user id end press <return> ==>
```
Type id# and then take photos. Photos are saved in dataset folder

### Training dataset :hourglass_flowing_sand:

Make directory to save a features file
```
pi@raspberrypi: ~ $ mkdir trainer
pi@raspberrypi: ~ $ python 02_face_training.py
```
train datasets in dataset directory using `recognizer.train(faces, np.array(ids))` and extract features and then save these features as a yaml file using `recognizer.write('trainer/trainer.yml')`
Now, go to trainer directory and check the yaml file

### Real-time face detection 
Now, detect face using trained and extracted features `trainer.yml`
```
pi@raspberrypi: ~ $ python 03_face_recognition.py
```
on the video window, a green square captures your face and shows name and matching percent.

Voila

> update more ...

Enjoy :)
