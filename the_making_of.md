# ROS notes

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

