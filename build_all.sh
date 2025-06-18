#!/bin/bash

WS=~/bt_ros/catkin_ws

echo "🔍 進入工作區：$WS"
cd $WS

# 🔥 如果有誤放入的 catkin source，刪除它
if [ -d "$WS/src/catkin" ]; then
    echo "⚠️ 偵測到 $WS/src/catkin，將其移除以避免干擾系統 catkin。"
    rm -rf "$WS/src/catkin"
fi

# 🧼 清理舊的 build/devel/log
echo "🧹 清理舊的 catkin 工作區"
catkin clean -y

# 🔁 設定 extend 到系統 ROS 安裝
echo "🔧 設定 extend 為 /opt/ros/melodic"
catkin config --extend /opt/ros/melodic

# 🔨 重新建構
echo "🚀 開始建構 Workspace"
catkin build -w $WS

echo "✅ 所有動作完成。請記得執行：source $WS/devel/setup.bash"

cd ..

