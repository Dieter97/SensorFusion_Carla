# Quick Start guide
This guide will explain how to quick start the application


## Starting the simulator

!!! Danger
    Todo

### Step 1: Starting the Carla Simulator
To start the carla simulator go to the Carla directory and type:

```shell
$ SDL_VIDEODRIVER=offscreen SDL_HINT_CUDA_DEVICE=0 ./CarlaUE4.sh
``` 

### Step 2: Starting Car.py
Car.py constains the code to spawn the Carla player actor alongside the sensors. This program will also start the Carla ROS bridge and open Rviz.
To do this, go to the SensorFusion_Carla directory and type:
```shell
$ source venv/bin/activate
$ python Car.py
```

## Starting the main programs

The main fusion program consists of a few nodes that need to be started:

!!! todo
    add links

- [cloud_crop](): will filter the lidar input cloud to output only camera visilbe points
- [clusteringCUDA](): will output clusters from the lidar point cloud
- [Lidar_object_fusion](): this is fusion system 1 (camera based)
- [Cluster_camera_fusion](): this is fusion system 2 (cluster based)
- [Lidar_camera_fusion](): this will output the camera image a mapped lidar point cloud on top

To start use the included launch file.

### Running using the simulator



### Running using the KITTI raw data set

!!! Alert
    This reqruires you to have downloaded the KITTI raw data sets as explained in [the evaluation process](evaluation.md)

Start the main fusion programm along with its required node:

```
roslaunch Lidar_object_fusion_KITTI.launch
- or -
roslaunch cluster_camera_fusion_KITTI.launch
- or -
roslaucnh lidar_camera_fusion_KITTI.launch
```

These launch files will start the required ROS nodes with correct parameters.

??? Help 
    - Camera input topic: /kitti/camera_color_left/raw
    - Lidar point cloud: /kitti/velodyne/points
    - COP: (0.054, 0, 0)
    - Scale factor: -3500
    - Camera plane: 0.27
    
    :exclamation: You can edit the launch file to match your needed parameters :exclamation:


### Running using real sensors

To launch the system to work on the BMW test car. This config is tested with the ZED camera and the VLP16 camera.

To launch:

```
roslaunch Lidar_object_fusion_BMW.launch
- or -
roslaunch cluster_camera_fusion_BMW.launch
- or -
roslaucnh lidar_camera_fusion_BMW.launch
```

These launch files will start the required ROS nodes with correct parameters.

??? Help 
    - Camera input topic: /zed/camera/left/raw
    - Lidar point cloud: /velodyne/pointcloud
    - COP: (0, 0, 0)
    - Scale factor: -4500
    - Camera plane: 0.35
    
    :exclamation: You can edit the launch file to match your needed parameters :exclamation:

