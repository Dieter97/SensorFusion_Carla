# Lidar_camera_fusion

This ROS node outputs the lidar point cloud projected on the image. The main purpose of this node is to verify the calibration parameters.

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
| cameraPlane | Defines the distance between the center of the camera and the center of the lidar | double |
| projectionScale | Scale parameter (mainly arbitrarily chosen) | double |
| copX, copY, copZ | 3D location of the lidar center relative to the camera center (in m) | double |


### Outputs

None

