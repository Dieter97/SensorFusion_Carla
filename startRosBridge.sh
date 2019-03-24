#!/bin/bash
# Carla Ros bridge starting script

echo "Starting ROS bridge!"
source /home/dieter/PycharmProjects/SensorFusion_Carla/venv/bin/activate
source /home/dieter/ros/catkin_ws_for_carla/devel/setup.bash

roslaunch carla_ros_bridge client_with_rviz.launch
