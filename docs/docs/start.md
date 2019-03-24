# Quick Start guide
This guide will explain how to quick start the application with the Carla Simulator

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

### Step 3: Starting the application
Start the nodes from the ros packages in the catkin_ws_sensorfusion workspace
