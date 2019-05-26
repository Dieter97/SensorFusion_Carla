# Quick Start guide
This guide will explain how to quick start the application


## Starting the simulator

!!! Info
    The code for the simulation can be found in the folder [Tech Report/code/SensorFusion_Carla](Tech Report/code/SensorFusion_Carla)

### Step 1: Starting the Carla Simulator
To start the carla simulator go to the Carla directory and type:

```shell
$ SDL_VIDEODRIVER=offscreen SDL_HINT_CUDA_DEVICE=0 ./CarlaUE4.sh
``` 

### Step 2: Starting Car.py
Car.py constains the code to spawn the Carla player actor alongside the sensors. This program will also start the Carla ROS bridge and opens Rviz.
To do this, go to the SensorFusion_Carla directory and type:
```shell
$ source venv/bin/activate
$ python Car.py
```

## Executing the fusion program

The main fusion program consists of a few nodes that need to be started:

- [cloud_crop](code/cloud_crop.md): will filter the lidar input cloud to output only camera visilbe points
- [clusteringCUDA](code/clustering.md): will output clusters from the lidar point cloud
- [Lidar_object_fusion](code/fusion1.md): this is fusion system 1 (camera based)
- [Cluster_camera_fusion](code/fusion2.md): this is fusion system 2 (cluster based)
- [Lidar_camera_fusion](code/lidar_camera.md): this will output the camera image a mapped lidar point cloud on top

!!! Help
    To execute the program use the included launch files.
   
    The launch files are located in [Tech Report/code/catkin_ws_sensorfusion/src/launch](Tech Report/code/catkin_ws_sensorfusion/src/launch)
    
    You can edit the parameters in the launch files themselves! For the evaluation you can edit the label parameter also in the launch file!

## Building program

The main sensor fusion code is located [Tech Report/code/catkin_ws_sensorfusion](Tech Report/code/catkin_ws_sensorfusion)
To compile the program go to the root directory of the catkin_ws_sensorfusion project and execute:

```
catkin_make
source devel/setup.bash
```

### Running using the simulator

??? Details

    
    Start the main fusion program along with its required node and the simulator config:
    
    ```
    cd catkin_ws_sensorfusion/src/launch
    roslaunch Lidar_object_fusion_CARLA.launch
    - or -
    roslaunch cluster_camera_fusion_CARLA.launch
    - or -
    roslaunch lidar_camera_fusion_CARLA.launch
    ```
    
    These launch files will start the required ROS nodes with correct parameters.
    
    ??? Help 
        - Camera input topic: /carla/ego_vehicle/camera/rgb/front/image_color
        - Lidar point cloud: /carla/ego_vehicle/lidar/front/point_cloud
        - COP: (0, 0, 0)
        - Scale factor: -2500
        - Camera plane: 0.2
        
        :exclamation: You can edit the launch file to match your needed parameters :exclamation:


### Running using the KITTI raw data set

??? Details

    !!! Alert
        This requires you to have downloaded the KITTI raw data sets as explained in [the evaluation process](evaluation.md)
    
    Start the main fusion program along with its required node and the KITTI config:
    
    ```
    cd catkin_ws_sensorfusion/src/launch
    roslaunch Lidar_object_fusion_KITTI.launch
    - or -
    roslaunch cluster_camera_fusion_KITTI.launch
    - or -
    roslaunch lidar_camera_fusion_KITTI.launch
    ```
    
    These launch files will start the required ROS nodes with correct parameters.
    
    ??? Help 
        - Camera input topic: /kitti/camera_color_left/image_raw
        - Lidar point cloud: /kitti/velo/pointcloud
        - COP: (0.054, 0, 0)
        - Scale factor: -3500
        - Camera plane: 0.27
        
        :exclamation: You can edit the launch file to match your needed parameters :exclamation:


### Running using real sensors (BMW)

??? Details

    To launch the system to work on the BMW test car. This config is tested with the ZED camera and the VLP16 LiDAR.
    
    Start the main fusion program along with its required node and the BMW config:
    
    ```
    cd catkin_ws_sensorfusion/src/launch
    roslaunch Lidar_object_fusion_BMW.launch
    - or -
    roslaunch cluster_camera_fusion_BMW.launch
    - or -
    roslaunch lidar_camera_fusion_BMW.launch
    ```
    
    These launch files will start the required ROS nodes with correct parameters.
    
    ??? Help 
        - Camera input topic: /zed/zed_node/left_raw/image_raw_color
        - Lidar point cloud: /velodyne_points
        - COP: (-0.08, 0, -0.02)
        - Scale factor: -4500
        - Camera plane: 0.2
        
        :exclamation: You can edit the launch file to match your needed parameters :exclamation:

