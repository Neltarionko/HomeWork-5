# HomeWork-5
Домашняя работа, целью которой являлось создание модели мобильного робота с дифференциальным приводом при помощи ROS2 Galactic Geochelone.

## Граф передачи сообщений между узлами системы: 
![alt text](https://github.com/Neltarionko/HomeWork-5/blob/main/image/rqt.jpg "Cтруктура проекта в виде графа")

Овалы - узлы системы


Прямоугольники - сообщения между узлами

## Сообщения проекта: 
![alt text](https://github.com/Neltarionko/HomeWork-5/blob/main/image/msg.jpg )

## Проверка отрисовки проекта: 
![alt text](https://github.com/Neltarionko/HomeWork-5/blob/main/image/odom.jpg "ТЕКСТ ПРИ НАВЕДЕНИИ")


## Состав работы
В результате работы было создано два пакета:
* sus - пакет типа ament-cmake для создания собственного системного сообщения;
* snarbot - пакет типа ament-python который принимает ввод с клавиатуры, выполняет необходимые преобразования и создаёт сообщения для узла визуализации rviz.

## Инструкция по запуску
### Шаг 1: Установка пакетов
1. Создать папку рабочего пространства
```
mkdir ~/ros_ws
cd ~/ros_ws
```
2. Склонировать содержимое репозитория
```
git clone https://github.com/Neltarionko/HomeWork-5
```
3. Меняем командную оболочку с Bash на ROS2
```
source /opt/ros/galactic/setup.bash
```
4. Необходимо собрать проект
```
colcon build
```
### Шаг 2: Запуск для проверки работоспособности
1. Создать 3 окна терминала, в каждом перейти в директорию рабочего пространства и сменить командную оболочку
```
cd ~/ros_ws
source /opt/ros/galactic/setup.bash
```
2. В первом терминале запустить узел TURTLEBOT3
```
export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_bringup rviz2.launch.py
```
3. Во втором терминале запустить публикатор узла snarbot
```
. install/local_setup.bash 
ros2 run snarbot publisher
```
4. В третьем терминале запустить средство визуализации rviz
```
export TURTLEBOT3_MODEL=waffle
ros2 run turtlebot3_teleop teleop_keyboard 
```

Управление роботом происходит посредством нажатия клавиш WASDX на клавиатуре в терминале с запущенным TURTLEBOT3. 

