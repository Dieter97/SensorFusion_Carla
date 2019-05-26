# Reports

This page lists all reports and other documents made for this thesis.

## Evaluation 

!!! Info
    Also the evaluation manual can be considered a report. Read it [here](Documentation/evaluation.md)
    
<a href="Evaluation Script.pdf" target="_blank">Open here in external viewer</a>

<embed src= "Evaluation Script.pdf" width= "700" height= "500">

## Future work

<a href="FutureWork.pdf" target="_blank">Open here in external viewer</a>

<embed src= "FutureWork.pdf" width= "700" height= "500">

## Schedules

<a href="UpdatedSchedule.pdf" target="_blank">Open here in external viewer</a>

<embed src= "UpdatedSchedule.pdf" width= "700" height= "500">

## Objective OLD

!!! Warning "Out-dated"
    This document is outdated. The scope of the thesis was updated during the course of the thesis.

<a href="Map-Research-Objective-MidTerm.pdf" target="_blank">Open here in external viewer</a>

<embed src= "Map-Research-Objective-MidTerm.pdf" width= "700" height= "500">

## Objective NEW

<a href="Map-Research-Objective-NEW.pdf" target="_blank">Open here in external viewer</a>

<embed src= "Map-Research-Objective-NEW.pdf" width= "700" height= "500">

## Algorithms

??? Example "Notes.md"
    
    # Sensor fusion algorithms notes 

    ### Camera based fusion
    
    Using detected objects from the camera to propose, then fusing this data with lidar points.
    Hyposthesis: 
    
    * High accuracy 
    * Slow
    * Needs image to detect any object (mud, fog,..)
    
    ### Cluster based fusion
    
    Using the lidar clusters to propsose objects that are then classified 
    Hyposthesis: 
    
    * Accuracy depends on resolution of lidar
    * Speed depends on clustering algorithm and number of clusters
    
    
    ### Object Tracking
    
    The current state of the application is situated on level 0 and level 1 of fusion
    
    Level 0: data aligment => time sync and coordinate transformation
    
    Level 1: fused objects
    
    ---
    
    ### Future improvments: 
    1. Level 1: object tracking + further property inference of the objects -> kalman filtering and Hungarian algorithm [link](https://www.ijert.org/research/an-efficient-tracking-of-multi-object-visual-motion-using-hungarian-method-IJERTV4IS041410.pdf)
    2. Level 2: situation refinement
    3. Level 3: Threat level assesment
    4. Level 4: Process refinement: optimizing the fusion process itself: ex. monitoring and updating offset parameters
   