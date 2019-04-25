# ROS notes

## Notes 4/25
### Actions
- connected our arduino nano to our motor shield using a breadboard a lots of tiny wires
- connected our motor shield to a 9v battery and two motors, tried out an example program to make sure they were hooked up right
- started looking at example projects to see how we'd handle velocity/twist commands

### Resources
- [our motor shield specs](https://www.arduino.cc/en/uploads/Main/arduino_MotorShield_Rev3-schematic.pdf)
- [the example code](https://www.instructables.com/id/Arduino-Motor-Shield-Tutorial/) that we used make the nano + motor shield control a motor
- [the example code](https://github.com/Reinbert/ros_diffdrive_robot/blob/master/ros_diffdrive_robot.ino) that we used to take velocity/twist commands from the pi and convert that into on/off commands for the motors

// our out ports
```
12, 9, 3
13, 8, 11
```

## Notes: 4/22
### What did we accomplish?
1. tried out the [blink tutorial](https://www.arduino.cc/en/tutorial/blink) to make sure everything was hooked up right
2. tried out a [rosserial_arduino tutorial](http://wiki.ros.org/rosserial_arduino/Tutorials/Hello%20World) to make our arduino publish messages

### Other notes
guides:
- https://www.arduino.cc/en/guide/environment
- http://wiki.ros.org/rosserial
- run `rosrun rosserial_python serial_node.py _port:=/dev/ttyUSB0 _baud:=115200` to make your arduino publish

our specific setup:
- Board: Arduino nano w/ ATMEGA328PA-PU
- Serial Port: ttyUSB0
- We had to run the arduino program as root

### Reminder
To ssh into our raspberry pi:
``` bash
ssh ubuntu@10.0.16.120
```


## Notes: 4/19
- [here's](https://gist.github.com/ngozinwogwugwu/f1fc6116ce4ade64d1e475bf516790f3) what we ended up making
- [What we used for our launch file](https://gist.github.com/WinKILLER/7a8f6aa494157f02a633efb3831ad69f)
- [depth image to laserscan](http://wiki.ros.org/depthimage_to_laserscan)
- to display CPU usage:
``` bash
htop
```


# Time to make the robot! Parts?
- We already have an [arduino motor sheild](https://www.dfrobot.com/product-1395.html?gclid=Cj0KCQjw4-XlBRDuARIsAK96p3CZOd7bPRxrw1fAHZBDwuc_uoWqofEITRjhjUJW-0A2Y0dPF2qBhRAaAvrkEALw_wcB)


## Notes: 4/15
- baseline: C++ function that looped through a point cloud and printed out the time it took. Was down to about 50 ms on the pi
- updated function to use an iterable instead of for-loop
- looped through point cloud to find the closest point
- program runs for a while, then crashes
- tried it on laptop. Program doesn't crash!
- there are still some problems: the "closest point" doesn't match up with what we'd expect. What's going on
- let's not do this in C++! This is terrible
- instead, let's: process the kinect inputs and publish Twist commands using Tim's laptop... in python. Then we can subscribe to the output using the raspberry pi

