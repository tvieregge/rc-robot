# Code for RC Robot
This robot isn't very clever, but it _should_ follow you around


# Components
- [Microsoft Kinect for Xbox One](https://www.amazon.com/Microsoft-L6M-00001-Kinect-for-Windows/dp/B006UIS53K)
- [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
- [Arduino nano w/ ATMEGA328PA-PU](https://store.arduino.cc/usa/nano-33-iot)
- [Arduino MotorShield Rev3](https://www.arduino.cc/en/uploads/Main/arduino_MotorShield_Rev3-schematic.pdf)
- Wheels, batteries and something to mount everything onto. In our case, it was a cutting board.

# How we did it
We ended up using [ROS](https://www.ros.org/) to route information from one component to another. For more information, take a look at [the making of](the_making_of.md)

# Resources
- [our motor shield specs](https://www.arduino.cc/en/uploads/Main/arduino_MotorShield_Rev3-schematic.pdf)
- [the example code](https://www.instructables.com/id/Arduino-Motor-Shield-Tutorial/) that we used make the nano + motor shield control a motor
- [the example code](https://github.com/Reinbert/ros_diffdrive_robot/blob/master/ros_diffdrive_robot.ino) that we used to take velocity/twist commands from the pi and convert that into on/off commands for the motors

