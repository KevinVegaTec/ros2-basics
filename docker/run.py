#!/usr/bin/env python

import os
import subprocess

# Function to check GPU availability
def check_gpu_availability():
    """
    This function checks if there is a GPU

    Returns:
        bool: The sum of the two numbers.
    """
    return os.path.exists("/dev/nvidia0")

# Check GPU availability
if check_gpu_availability():
    GPU_SUPPORT = "--runtime=nvidia"
    GPU_MESSAGE = "with GPU support"
else:
    GPU_SUPPORT = ""
    GPU_MESSAGE = "without GPU support"

# Customize your ROS container command based on GPU availability
DOCKER_COMMAND = f"docker run {GPU_SUPPORT} -it -d \
    -e LOCAL_USER_ID \
    -e LOCAL_GROUP_ID \
    -e LOCAL_GROUP_NAME \
    -e DISPLAY \
    -e QT_X11_NO_MITSHM=1 \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v {os.getcwd()}/ros2_ws/src:/ros2_ws/src \
    -v {os.getcwd()}/ros2_ws/typings:/ros2_ws/typings \
    --network host \
    --privileged \
    --name ros2-base \
    ros2:base \
    bash"

# Build your ROS workspace inside the container
ROS_BUILD_COMMAND = "docker exec -it ros2-base /bin/bash -c 'cd /ros2_ws && . /opt/ros/humble/setup.bash && colcon build'"

# Run your ROS container
subprocess.run(DOCKER_COMMAND, shell=True, check=True, executable='/bin/bash')

print(f"ROS container started {GPU_MESSAGE}")

# Execute the ROS build command
subprocess.run(ROS_BUILD_COMMAND, shell=True, check=True, executable='/bin/bash')

print("ROS workspace built")
