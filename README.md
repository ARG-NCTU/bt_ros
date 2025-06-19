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

## 🧱 Build the Catkin Workspace (Inside Docker)

```bash
cd catkin_ws
catkin build
```

---

## 🚀 Run the Demo

```bash
make demo_test
```
