#include <ctime>
#include <iostream>
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sensor_msgs/PointCloud2.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>

ros::Publisher pub;

void chatterCallback(const sensor_msgs::PointCloud2ConstPtr& input)
{
    std::clock_t    start;
    start = std::clock();
    // Create a container for the data.
  /* sensor_msgs::PointCloud2 output; */

  // Container for original & filtered data
  /* pcl::PCLPointCloud2* cloud = new pcl::PCLPointCloud2; */
  /* pcl::PCLPointCloud2ConstPtr cloudPtr(cloud); */

  // Convert to PCL data type
  /* pcl_conversions::toPCL(*input, *cloud); */
  pcl::PointCloud<pcl::PointXYZ>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZ>);
  pcl::fromROSMsg (*input, *cloud);

  // Do data processing here...
  /* output = *input; */
  /* for (auto v : cloud->data) { */
 //   printf("%d", cloud->data[0]);
  /* } */

    pcl::PointCloud<pcl::PointXYZ>::iterator it;
    for(it = cloud->begin(); it != cloud->end(); it++){
        std::cout << it->x << ", " << it->y << ", " << it->z << std::endl;
    }

  // Publish the data.
  /* pub.publish (output); */
  std::cout << "Time: " << (std::clock() - start) / (double)(CLOCKS_PER_SEC / 1000) << " ms" << std::endl;
}

int main(int argc, char **argv)
{
  /**
   * The ros::init() function needs to see argc and argv so that it can perform
   * any ROS arguments and name remapping that were provided at the command line.
   * For programmatic remappings you can use a different version of init() which takes
   * remappings directly, but for most command-line programs, passing argc and argv is
   * the easiest way to do it.  The third argument to init() is the name of the node.
   *
   * You must call one of the versions of ros::init() before using any other
   * part of the ROS system.
   */
  ros::init(argc, argv, "listener");

  /**
   * NodeHandle is the main access point to communications with the ROS system.
   * The first NodeHandle constructed will fully initialize this node, and the last
   * NodeHandle destructed will close down the node.
   */
  ros::NodeHandle n;

  /**
   * The subscribe() call is how you tell ROS that you want to receive messages
   * on a given topic.  This invokes a call to the ROS
   * master node, which keeps a registry of who is publishing and who
   * is subscribing.  Messages are passed to a callback function, here
   * called chatterCallback.  subscribe() returns a Subscriber object that you
   * must hold on to until you want to unsubscribe.  When all copies of the Subscriber
   * object go out of scope, this callback will automatically be unsubscribed from
   * this topic.
   *
   * The second parameter to the subscribe() function is the size of the message
   * queue.  If messages are arriving faster than they are being processed, this
   * is the number of messages that will be buffered up before beginning to throw
   * away the oldest ones.
   */
  ros::Subscriber sub = n.subscribe("camera/depth_registered/points", 1000, chatterCallback);
  pub = n.advertise<sensor_msgs::PointCloud2>("chatter2", 1000);

  /**
   * ros::spin() will enter a loop, pumping callbacks.  With this version, all
   * callbacks will be called from within this thread (the main one).  ros::spin()
   * will exit when Ctrl-C is pressed, or the node is shutdown by the master.
   */
  ros::spin();

  return 0;
}
