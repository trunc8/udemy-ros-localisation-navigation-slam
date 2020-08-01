#include <ros/ros.h>
#include <tf/transform_broadcaster.h>

int main(int argc, char** argv){
    ros::init(argc, argv, "frame_a_frame_b_broadcaster");
    ros::NodeHandle node;

    tf::TransformBroadcaster br;
    tf::Transform transform;

    ros::Rate rate(2.0);
    while (node.ok()) {
        transform.setOrigin( tf::Vector(1,2,3) );
        transform.setRotation( tf::Quaternion(0, 0, 0, 1) );
        br.sendTransform(tf::stampedTransform(transform, ros::Time::now(),
            "frame_b","frame_a"));
        rate.sleep();
    }
    return 0;
};
