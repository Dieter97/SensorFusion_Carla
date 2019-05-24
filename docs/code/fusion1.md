# Lidar_object_fusion

### Overview
This is the fist fusion system as proposed in my paper.
This ROS node will fuse the lidar and camera sensor input based on camera proposed ROI's.

### Inputs

|  Parameter name |  Description  |  Type  |
|-----------------|---------------|--------|
|  input  	|  preprocessed cloud (cloud_crop output)	| Pointcloud2 |
|  cameraInput  	|  raw camera input	| Image |



### Outputs

|  Parameter name |  Description  |  Type  |
|-----------------|---------------|--------|
|  output  	| separate clusters	|  sensor_fusion_msg/LidarClusters |


