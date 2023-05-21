# HomeWork-5

## Состав работы
В результате работы было создано два пакета:
* sus
* snarbot

1 термирминал запуск ноды
source /opt/ros/galactic/setup.bash
colcon build
. install/local_setup.bash 
ros2 run snarbot publisher 

2 терминал запус rviz
source /opt/ros/galactic/setup.bash
export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_bringup rviz2.launch.py 

3 терминал запус клавиатуры
source /opt/ros/galactic/setup.bash
export TURTLEBOT3_MODEL=waffle
ros2 run turtlebot3_teleop teleop_keyboard 
