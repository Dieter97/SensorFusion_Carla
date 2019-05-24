# clusteringCUDA

### Overview

!!! Danger
    This node requires CUDA 10.0 and PCL 1.9 to be correctly installed 

This ROS node outputs cluster from a raw point cloud. In the main system this node is placed after the cloud_crop node. 
This node requires a GPU.


### Inputs

#### Topic:

|  Topic name |  Description  |  Type  |
|-----------------|---------------|--------|
|  input  	|  preprocessed cloud (cloud_crop output)	| Pointcloud2 |

#### Other parameters:

!!! Warning
    Every parameter is required!

|  Parameter name |  Description  |  Type  |
|-----------------|---------------|--------|
|  threshold  	|  Threshold used by the euclidean clustering algorithm (ex. 2,1)	| double |

### Outputs

|  Topic name |  Description  |  Type  |
|-----------------|---------------|--------|
|  output  	| separate clusters	|  sensor_fusion_msg/LidarClusters |
