# Lidar_object_fusion

### Overview
This is the fist fusion system as proposed in my paper.
This ROS node will fuse the lidar and camera sensor input based on camera proposed ROI's.

### Inputs

#### Topics:

|  Topic Name |  Description  |  Type  |
|-----------------|---------------|--------|
|  input  	|  preprocessed cloud (cloud_crop output) (default: /lidar/detection/out/cropped)	| Pointcloud2 |
|  cameraInput  	|  raw camera input	| Image |

#### Other parameters:

!!! Warning
    Every parameter is required!

|  Parameter Name |  Description  |  Type  |
|-----------------|---------------|--------|
| bufferSize | This defines how many messages the node should buffer | int |
| label | This defines where the node should output the evaluation label files (get ignored if this path doesnt exist) | String
| cameraPlane | Defines the distance between the center of the camera and the center of the lidar | double |
| projectionScale | Scale parameter (mainly arbitrarily chosen) | double |
| copX, copY, copZ | 3D location of the lidar center relative to the camera center (in m) | double |
| darknetCfg | The darknet model config file (Yolo) | String |
| darknetWeights | The darknet model weight file | String |
| darknetDataSet | The darknet label data set file (COCO) | String |


### Outputs

|  Topic Name |  Description  |  Type  |
|-----------------|---------------|--------|
|  /camera/detection/out/image  | output image	|  sensor_fusion_msg/LidarClusters |
|  /fusion/bounding/out_array  | 3D bounding boxes output	| visualization_msgs/Marker (Array) |
|  /fusion/objects/out | Fused object outputs	| sensor_fusion_msg/FusedObjectsMsg |


