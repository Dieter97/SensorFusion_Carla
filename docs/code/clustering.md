# clusteringCUDA

### Overview

!!! Warning
    This node requires CUDA 10.0 and PCL 1.9 to be correctly installed 

This ROS node outputs cluster from a raw point cloud. In the main system this node is placed after the cloud_crop node. 
This node requires a GPU.


### Inputs

|  Parameter name |  Description  |  Type  |
|-----------------|---------------|--------|
|  input  	|  preprocessed cloud (cloud_crop output)	| Pointcloud2 |


### Outputs

|  Parameter name |  Description  |  Type  |
|-----------------|---------------|--------|
|  output  	| separate clusters	| Pointcloud2 |
