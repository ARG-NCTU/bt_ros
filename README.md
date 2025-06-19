# Project Setup Guide

This guide provides step-by-step instructions to build and run the Docker container for your ROS workspace.

---

## 🔧 Build the Docker Container

```bash
source docker_build.sh
```

---

## 🚪 Enter the Docker Container

```bash
source docker_run.sh
```

---

## 🧱 Build the Catkin Workspace (First time)

```bash
cd catkin_ws
catkin build
```

---

## 🚀 Run the Demo

```bash
source script/00_setup_all.sh
make demo_test
```
