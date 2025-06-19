FROM nvidia/cuda:11.0.3-cudnn8-devel-ubuntu18.04

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV ROS_DISTRO=melodic

###################################### user #####################################

ENV SHELL=/bin/bash \
    NB_USER=argnctu \
    NB_UID=1000 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

RUN adduser --disabled-password --gecos "Default user" --uid ${NB_UID} ${NB_USER} 
RUN echo "root:root" | chpasswd
RUN echo "${NB_USER}:111111" | chpasswd
ENV HOME=/home/${NB_USER}

##################################### base tools #####################################
RUN apt-get -o Acquire::ForceIPv4=true update && apt-get -yq dist-upgrade && \
    apt-get -o Acquire::ForceIPv4=true install -yq --no-install-recommends \
    curl vim wget sudo cmake gedit gnupg2 gtk+-3.0 locales dirmngr mercurial \
    net-tools lsb-release openssh-client build-essential libcanberra-gtk-module \
    libcanberra-gtk3-module libpcap-dev libusb-1.0 tzdata libglfw3-dev \
    libmetis-dev python-gtk2 python-gobject python-tk software-properties-common \
    ruby python3-pip python3-setuptools python3-venv python3-dev python3-tk \
    python3-yaml bash-completion git fluid xterm scrot qtbase5-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 時區設定
RUN export DEBIAN_FRONTEND=noninteractive && apt update && apt install -y tzdata && \
    ln -fs /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && apt clean

###################################### ROS core #####################################
RUN echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list && \
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-${ROS_DISTRO}-desktop-full \
    python-catkin-tools python-rosdep python-rosinstall python-rosinstall-generator \
    python-wstool python-vcstool && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN rosdep init && rosdep update

# 新增 rosdep 安裝依賴步驟
RUN mkdir -p /home/${NB_USER}/bt_ros/catkin_ws/src && \
    rosdep install --from-paths /home/${NB_USER}/bt_ros/catkin_ws/src --ignore-src -y -r

##################################### Python 2/3 packages #####################################
RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py && python2 get-pip.py
RUN pip2 install --upgrade pip setuptools
RUN pip2 install pytest

RUN pip3 -V && pip3 install --upgrade pip setuptools
RUN pip3 install \
    requests \
    jupyter \
    jupyter_http_over_ws \
    rospkg \
    "catkin-tools<0.9.0" \
    pyautogui \
    wheel

####################################### procman ###########################################

RUN cd ${HOME} && git clone -b v1.5.0 --single-branch https://github.com/lcm-proj/lcm \
    && cd lcm \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make install \
    && cd .. \
    && cd lcm-python \
    && python setup.py install

RUN cd ${HOME} && git clone http://github.com/ARG-NCTU/procman \
    && cd procman \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make install

################################# mkdocs & plugins #################################
RUN pip3 install \
    mkdocs \
    mkdocs-with-pdf \
    mkdocstrings \
    mkdocs-material \
    "mkdocstrings[python]"

RUN cd ${HOME} && git clone https://github.com/fralau/mkdocs-mermaid2-plugin.git && \
    cd mkdocs-mermaid2-plugin && \
    python3 setup.py install

##################################### xdotool & wmctrl #####################################
RUN apt-get update && apt-get install -y --no-install-recommends xdotool wmctrl

##################################### bashrc & NVIDIA Docker support #####################################
RUN echo "root ALL=(ALL)  ALL" >> /etc/sudoers && \
    echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ${HOME}/.bashrc 

ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=all

