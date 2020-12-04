## :black_heart: [YOLO](https://pjreddie.com/darknet/yolo/) object detection 

Prerequisites : Raspberry pi 4, darknet, and YOLO v.3

### Install darknet and YOLO :crystal_ball:
Open terminal and download darknet

```
pi@raspberrypi: ~ $ git clone https://github.com/AlexeyAB/darknet
pi@raspberrypi: ~ $ cd darknet
pi@raspberrypi: ~/darknet $ make
``` 

![01_darknet_install](https://user-images.githubusercontent.com/40614421/101201926-c4221a00-3668-11eb-876e-de2e617cff94.jpg)

Then, download YOLO v.3 using `wget`

``` 
pi@raspberrypi: ~/darknet $ wget https://pjreddie.com/media/files/yolov3.weights
``` 

![02_yolo](https://user-images.githubusercontent.com/40614421/101201800-95a43f00-3668-11eb-96ef-14a6129f479d.png)

YOLO v.3 is downloading ...

![03_yolo_install](https://user-images.githubusercontent.com/40614421/101199525-4c9ebb80-3665-11eb-824d-8c022aa20c94.png)

### Detection :: Image :camera:

``` 
pi@raspberrypi: ~/darknet $ ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
``` 
If you want to try with your own photo, copy your photo in `/darknet/data` and run it.
For example, prepare `catdog.png` :dog: :cat:

![04_01_catdog](https://user-images.githubusercontent.com/40614421/101199547-56282380-3665-11eb-8b62-dadcb59cf187.jpg)

Then, run the detector again

``` 
pi@raspberrypi: ~/darknet $ ./darknet detect cfg/yolov3.cfg yolov3.weights data/catdog.jpg
```

Check output what the model detects

![04_02_cat_dog_result](https://user-images.githubusercontent.com/40614421/101199570-617b4f00-3665-11eb-8d9f-283b2cdecd30.png)

and result is saved in `prediction.png` becuase it cannot be compiled with OpenCV

![04_03_cat_dog_prediction](https://user-images.githubusercontent.com/40614421/101199595-6dffa780-3665-11eb-8cec-fa875791255a.png)

Another example :dog: :heartbeat:

![05_01_Loup](https://user-images.githubusercontent.com/40614421/101199901-db133d00-3665-11eb-896c-e2deb67fc55e.jpeg)

Okay, check the output (prediction)
The pretrained model detects dog, chair, dining table and sport ball :sunglasses:

![05_03_Loup_prediction](https://user-images.githubusercontent.com/40614421/101199922-e5353b80-3665-11eb-9a1c-27346235651d.jpg)

### Detection :: Video :video_camera:
Now, try with video
> coming soon...

Enjoy :)
