# tello-quad
[Ryze/DJI/Intel Tello Drone](https://www.ryzerobotics.com/tello?utm_source=dji&utm_medium=store&utm_campaign=product_page)
quadcopter research and development.
## Table of Contents
- [INSTALL](#install)
- [RESEARCH](#research)
- [DEVELOPMENT](#development)
## INSTALL
```console
$ git clone https://github.com/pdinkins/tello-quad.git
```
## RESEARCH
### Documentation
- [User Manual](https://dl-cdn.ryzerobotics.com/downloads/Tello/20180404/Tello_User_Manual_V1.2_EN.pdf)
- [Tello SDK](https://terra-1-g.djicdn.com/2d4dce68897a46b19fc717f3576b7c6a/Tello%20%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3/For%20Tello/Tello%20SDK%20Documentation%20EN_1.3_1122.pdf)
- [Tello3.py](https://terra-1-g.djicdn.com/2d4dce68897a46b19fc717f3576b7c6a/Tello%20%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3/Both/Tello3(1).py)
### Repositories
- [damiafuentes/DJITelloPy](https://github.com/damiafuentes/DJITelloPy)
        - DJI Tello drone python interface using the official Tello SDK. Yes, this library has been tested with the drone. Please see example.py for a working example controlling the drone as a remote controller with the keyboard and the video stream in a window.
- [dji-sdk/Tello-Python](https://github.com/dji-sdk/Tello-Python)
        - This is a collection of python-based sample code that interact with the Ryze Tello drone. This toolkit contains three sample programs based on tello sdk and python2.7,including Single_Tello_Test, Tello_Video, and Tello_Video (With_Pose_Recognition). There is also a program file named tello_state.py.
- [microlinux/tello](https://github.com/microlinux/tello)
        - This code and documentation is based on the Tello SDK documentation as of 3/19/2018.A Python interface for the Ryze Tello drone. The tello module provides a Tello class, which interacts with the Tello API.
- [hanyazou/TelloPy](https://github.com/hanyazou/TelloPy)
        - This is a python package which controlls DJI toy drone 'Tello'. The major portion of the source code was ported from the driver of GOBOT project. For original golang version and protocol in detail, please refer their blog post at [gobot.io](https://gobot.io/blog/2018/04/20/hello-tello-hacking-drones-with-go)
- [Jabrils/TelloTV](https://github.com/Jabrils/TelloTV)
        - TelloTV is a rather simplistic approach to be able to launch your Tello drone & hav it track your face. This approach has been tested & proven to work with the DJI Tello Drone (Non - Educational Version I believe, but may still work with the educational version?)
- [parakhm95/Ryze-Tello-Position-Controller](https://github.com/parakhm95/Ryze-Tello-Position-Controller)
        - This is a collection of python-based sample code that interact with the Ryze Tello drone.
### Download research libraries
```console
$ cd tello-quad/research
$ python3 main.py
```
### Videos
- [Jabrils - 🖥️ I Made an AI Drone That Tracks Any Face!](https://www.youtube.com/watch?v=esw88_gKOpA&feature=youtu.be)
- [Wes Bos - Flying a Drone with React and Node.js! (100% JavaScript!) — PART 1](https://www.youtube.com/watch?v=JzFvGf7Ywkk)
- [Wes Bos - Flying a Drone with React and Node.js! (100% JavaScript!) — PART 2](https://www.youtube.com/watch?v=ozMwRq-IT2w)
- [Dennis Baldwin - Tello EDU Drone Swarming Tutorial with Packet Sender and Python](https://www.youtube.com/watch?v=cIsddY4SKgA)
- [Dave Briccetti - Raspberry Pi, Rangefinder and Python Fly a Tello Drone](https://www.youtube.com/watch?v=_dN_helpT0A)
- [Heliguy - How to connect the Tello drone to Scratch coding software](https://www.youtube.com/watch?v=-M7dCeb6fMY)
- [CloudLove - TensorFlow - DJI Tello - Object Recognition](https://www.youtube.com/watch?v=qmhspfHoPQU)
- [James Williams - Tello Drone - Python API Test ](https://www.youtube.com/watch?v=zFH_BkG6tBI)
- [Meisech - Ryze Tello - Part 3 - Programming the Tello step by step](https://www.youtube.com/watch?v=usxynMuEqEA)
## DEVELOPMENT