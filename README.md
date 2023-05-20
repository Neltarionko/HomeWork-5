# HomeWork-5

1 термирминал запуск ноды
colcon build
. install/local_setup.bash 
ros2 run snarbot publisher 

2 терминал запус rviz
export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_bringup rviz2.launch.py 

3 терминал запус клавиатуры
export TURTLEBOT3_MODEL=waffle
ros2 run turtlebot3_teleop teleop_keyboard 
