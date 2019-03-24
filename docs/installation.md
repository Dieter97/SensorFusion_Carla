# Installation
This page guides the installation on ubuntu 18.04 Bionic. Please take in mind everything listed here is required!

## Nvidia driver and Cuda Toolkit
The required versions are:

!!! Important "Nvidia Versions"
    + Nivdia driver 410+
    + [Cuda Toolkit 10.0](https://developer.nvidia.com/cuda-10.0-download-archive)
    + [CuNN](https://developer.nvidia.com/cudnn) : only if GPU supports it (tensorcores)
To check your version:
```
$ nvidia-smi
```

## ROS Melodic
Follow the installation guide for [ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu).
It is recommended to install the full desktop version:
```shell
$ sudo apt install ros-melodic-desktop-full
```
## Carla
* Download the [latest](https://github.com/carla-simulator/carla/blob/master/Docs/download.md) Carla version 

* Download and compile the [latest](https://github.com/carla-simulator/ros-bridge) Carla ROS bridge

!!! Warning "Carla Version"
    The system is developed with Carla-0.9.4! At the time of reading this the version may be changed as well as some functionallity.

## OpenCV
Best is to compile yourself: [openCV](https://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html)

## Camera dependencies
##### DARKNET
To run the camera object detection node, Darknet is required:
to install follow these steps:
```shell
$ cd ~/
$ git clone https://github.com/pjreddie/darknet
$ cd darknet
```
Open the `Makefile` and change the first lines to the following:
```c++
GPU=1
CUDNN=0 // Can be one if GPU supports it and CuDNN is installed
OPENCV=1
OPENMP=0
DEBUG=0
```
!!! warning
    This requires you have the Cuda toolkit installed and openCV
Then build Darknet:
```shell 
$ make
```
Now Darknet is ready to be used. Predtrained models can be found [here]()
!!! Important
    To use the coco dataset in the file `{darknet-dir}/cfg/coco.data` the line `names` needs to be changed:
    names = /home/dieter/darknet/data/coco.names

## LiDAR dependencies

The LiDAR requires the Point Cloud Library. This library comes inluded with ROS but not the GPU modules. Therefore compiling yourself is the best option

!!! Important
    This also requires the Cuda toolkit 10.0 is installed and the nvcc tool is working

##### PCL 1.9
To compile PCL 1.9:
```shell
$ cd ~/
$ git clone https://github.com/PointCloudLibrary/pcl.git
$ cd pcl-pcl-{verions}
$ mkdir build; cd build
$ ccmake ..
```
In ccmake enable advanced mode by pressing 't'. Then enable the GPU and CUDA packages. To exit the press 'c' to configure and 'g' to generate makefiles, then exit.
```shell
$ make -j7
$ make install
```






