# Evaluation

The evaluation benchmark used in this research is the [KITTI benchmark](http://www.cvlibs.net/datasets/kitti/). 
The included evaluation script used label files from two sources: 

- KITTI label files as ground truth
- Generated label files: the detected objects from the algorithms

### Getting started with the KITTI raw data set

#### Download
To run a benchmark data is needed. The data can be found on [this page](http://www.cvlibs.net/datasets/kitti/raw_data.php)
Download one of these data sets. You need the synced+rectified data, calibration, and tracklets files.

!!! Example
    Example for data set 1:
    
    ```shell
    wget https://s3.eu-central-1.amazonaws.com/avg-kitti/raw_data/2011_09_26_drive_0001/2011_09_26_drive_0001_sync.zip
    wget https://s3.eu-central-1.amazonaws.com/avg-kitti/raw_data/2011_09_26_calib.zip
    wget https://s3.eu-central-1.amazonaws.com/avg-kitti/raw_data/2011_09_26_drive_0001/2011_09_26_drive_0001_tracklets.zip
    ``` 

#### Unzip
Next unzip everything in order to get the folowing structure:

```
2011_09_26/
├── 2011_09_26_drive_0001_sync
│   ├── image_00
│   │   └── data
│   ├── image_01
│   │   └── data
│   ├── image_02
│   │   └── data
│   ├── image_03
│   │   └── data
│   ├── oxts
│   │   └── data
|   ├── tracklet_labels.xml
│   └── velodyne_points
│       └── data
├── calib_cam_to_cam.txt
├── calib_imu_to_velo.txt
└── calib_velo_to_cam.txt
```

### Generate ROSbag from KITTI data set
To generate a ROS bag from the downloaded data set install kitti2bag

```
pip install kitti2bag
```

Then execute the following to generate the rosbag file:
```
kitti2bag -t 2011_09_26 -r 0001 raw_synced .
```

### Start the rosbag and run the fusion algorithm
First start the fusion program itself as explained in a previous manual.


!!! info
    To run with the rosbag the topic input topic are:
    
    - /kitti/camera_gray_left/image_raw
    - /kitti/camera_color_left/image_raw
    - /kitti/velo/pointcloud


Next start the rosbag play:
```
rosbag play kitti_2011_09_26_drive_0001_synced.bag
```

This should now run and generate a xxxxxx.txt label file per frame in the output directory.

### Preparing the evaluation script

The evaluation script needs ground truth data to be able to evaluate the detected objects. This ground truth data comes in the form of label file. 
The label files for each frame can be generated from the `tracklet_labels.xml` file downloaded earlier.
To generate these xxxxxx.txt label files run the `tracklet_to_label.m` matlab script. You will need to change the parameters of the script in matlab itself.
You must locate the earlier downloaded data set, and specify a output location.

To run the evaluation script you ideally end up with this structure:

```
eval/
├── results
|   ├── data
|   |    ├── 000001.txt
|   |    ├── ...
|   |    └── xxxxxx.txt
├── ground
|   ├── data
|   |    ├── 000001.txt
|   |    ├── ...
|   |    └── xxxxxx.txt
```

### Running the evaluation script

If all previous step are completed and you now have a both detected label files and ground truth label files, you can run the evaluation script:

??? Help
    For more help:
    ```
    python eval.py -h
    ```

```
python eval.py [result folder] [ground truth folder]
```