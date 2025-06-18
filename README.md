# ARG Drone Repo
This repo consist of the ROS interface for the drone used in research. Can be use with px4 sitl simulation with gazebo to test the code first and migrate to the real drone.

# Setup
```
$: means command use in terminal  
#: means command use in docker terminal  

```
## 1.Clone the repo
```
$ cd ~
$ git clone --recursive git@github.com:ARG-NCTU/vr_llm_aerial_manipulation.git
```
## 2.Update repo and submodules

```bash
$ git pull
$ git submodule sync --recursive
$ git submodule update --init --recursive
```

## 3.download Env Mesh model (if you use this repo for real drone, skip this step)
```
$ cd ~/vr_llm_aerial_manipulation/scripts
$ source download_env_mesh.bash
```
Follow the example input you can download the environment mesh model for simulation in gazebo. 

## 4.QGC
### Install QGC
```
$ ~/vr_llm_aerial_manipulation$ source scripts/download_QGC.bash
```
### Setup QGC
```
$ ~/vr_llm_aerial_manipulation$ source scripts/setup_QGC.sh 
```
```
$ sudo reboot
```

## 5. Build ROS workspace
* Check the device you are using (if you use workstation please use ipc_run.sh, if you use real_drone with nuc, use nuc_run.sh)
```
$ cd ~/vr_llm_aerial_manipulation
~/vr_llm_aerial_manipulation$ source ipc_run.sh
~/vr_llm_aerial_manipulation# source build_all.sh
```
After build_all script finish, all setup complete you can check [aerial_manipulation_sim](https://github.com/ARG-NCTU/vr_llm_aerial_manipulation/blob/master/tutorial/Aerial_manipulation_sim.md), [aerial_manipulation_real](https://github.com/ARG-NCTU/vr_llm_aerial_manipulation/blob/master/tutorial/Aerial_manipulation_real.md), and [aerial_sim_lab](https://github.com/ARG-NCTU/vr_llm_aerial_manipulation/blob/master/tutorial/Aerial_simulation_lab.md) for how to run the code of aerial related task. 

# How to run example
For this example how to run you can run the simulation drone without manipulator in gazebo empty world environment.

## Terminal 1: QGC for monitor drone status
```
$ ./QGroundControl.AppImage
```
## Terminal 2: Start simulation environment in docker
* To run docker the first terminal we will use xxx_run.sh and following second third ... terminal we will use xxx_join.sh
### Start docker 
``` 
$ cd ~/vr_llm_aerial_manipulation
~/vr_llm_aerial_manipulation$ source ipc_run.sh
```
### Load environment setup parameter
* 00_setup_all.sh will copy the environment.sh to .bashrc so just do one time.
```
~/vr_llm_aerial_manipulation# source scripts/00_setup_all.sh
```
### Launch the gazebo simulation environment
```
~/vr_llm_aerial_manipulation# roslaunch drone_gazebo if750a.launch 
```
## Terminal 3: Extra terminal you can use rqt, rviz application
### Join docker 
``` 
$ cd ~/vr_llm_aerial_manipulation
~/vr_llm_aerial_manipulation$ source ipc_join.sh
```
### Run rqt or rviz etc...
* rqt
```
~/vr_llm_aerial_manipulation# rqt
```
* rviz
```
~/vr_llm_aerial_manipulation# rviz
```
* You can use QGC to control drone flying. 