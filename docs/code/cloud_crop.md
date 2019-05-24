# Cloud_crop

### Overview

!!! Warning
    This node requires PCL 1.9 to be correctly installed

This ROS node take in a raw point cloud and will preprocess this cloud in three main steps:

- Downsample the raw cloud with a leaf size of 0.5 (not configurable)
- Crop the point cloud to only output camera visible points 
- Find a remove the ground plane using the RANSAC algorithm

### Inputs

|  Parameter name |  Description  |  Type  |
|-----------------|---------------|--------|
|  input  	|  raw sensor point cloud	| Pointcloud2 |


### Outputs

|  Topic name |  Description  |  Type  |
|-----------------|---------------|--------|
|  /lidar/detection/out/cropped  	| the processed point cloud	| Pointcloud2 |
