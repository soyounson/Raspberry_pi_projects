:black_heart: [YOLO](https://pjreddie.com/darknet/yolo/) object detection 

Prerequisites : Raspberry pi 4, darknet, YOLO v.3

### Install darknet and YOLO :crystal_ball:
open terminal and download darknet

```
pi@raspberrypi: ~ $ git clone 
pi@raspberrypi: ~ $ cd darknet
pi@raspberrypi: ~/darknet $ make
``` 
<div>
![01_darknet_install](https://user-images.githubusercontent.com/40614421/101198190-5d4e3200-3663-11eb-8a95-c6ac2d5b99b9.png)
</div>

Then, download YOLO v.3 using wget

``` 
pi@raspberrypi: ~/darknet $ wget https://pjreddie.com/media/files/yolov3.weights
``` 

<div>
![02_yolo](https://user-images.githubusercontent.com/40614421/101199499-427cbd00-3665-11eb-9316-4d79c31bbff5.png)
</div>

YOLO v.3 is downloading ...

<div>
![03_yolo_install](https://user-images.githubusercontent.com/40614421/101199525-4c9ebb80-3665-11eb-824d-8c022aa20c94.png)
</div>

### Detection :: Image :camera:

``` 
pi@raspberrypi: ~/darknet $ ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
``` 
If you run your photo, move your photo in `/darknet/data` and run it.
For example, prepare `catdog.png` :dog: :cat:

<div>
![04_01_catdog](https://user-images.githubusercontent.com/40614421/101199547-56282380-3665-11eb-8b62-dadcb59cf187.jpg)
</div>

then, run the detector again

``` 
pi@raspberrypi: ~/darknet $ ./darknet detect cfg/yolov3.cfg yolov3.weights data/catdog.jpg
``` 
check output what the model detects

<div>
![04_02_cat_dog_result](https://user-images.githubusercontent.com/40614421/101199570-617b4f00-3665-11eb-8d9f-283b2cdecd30.png)
</div>

and result is saved in `prediction.png` becuase it cannot be compiled with OpenCV

<div>
![04_03_cat_dog_prediction](https://user-images.githubusercontent.com/40614421/101199595-6dffa780-3665-11eb-8cec-fa875791255a.png)
</div>

Another example with my dog :dog:

<div>
![05_01_Loup](https://user-images.githubusercontent.com/40614421/101199901-db133d00-3665-11eb-896c-e2deb67fc55e.jpeg)
</div>

see output (prediction)
The pretrained model detects dog, chair, dining table and sport ball :)

<div>
![05_03_Loup_prediction](https://user-images.githubusercontent.com/40614421/101199922-e5353b80-3665-11eb-9a1c-27346235651d.jpg)
</div>


### Detection :: Video :video_camera:
Now, try with video


Enjoy :)
