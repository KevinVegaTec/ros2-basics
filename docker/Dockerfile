FROM osrf/ros:humble-desktop-full
LABEL maintainer="vegakevinrdz@gmail.com"
LABEL version="1.0"
LABEL build_date="23/10/2023"
LABEL description="Simple ROS 2 container"

RUN apt-get update -qq && \
    apt-get install -y \
    build-essential \
    nano \
    git \
    autoconf \
    libtool \
    python3-pip \
    mesa-utils \
    python3-colcon-common-extensions 


RUN rm -rf /var/lib/apt/lists/*

RUN mkdir /ros2_ws
COPY ros2_ws /ros2_ws
WORKDIR /ros2_ws
RUN /bin/bash -c '. /opt/ros/humble/setup.bash;colcon build'

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "[ -f /ros2_ws/install/setup.bash ] && source /catkin_home/install/setup.bash" >> ~/.bashrc

ENTRYPOINT [ "/bin/bash", "-l" ]