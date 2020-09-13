## Udemy\_ROS\_Part2
[Notes](https://nbviewer.jupyter.org/github/trunc8/udemy_ros_part2/blob/master/Udemy_ROS_Part2_Notes.pdf) written by me and code replicated (from scratch) while completing the Udemy Course delivered by Anis Koubaa titled [ROS For Beginners II: Localization, Navigation and SLAM](https://www.udemy.com/course/ros-navigation/)


| Description | Screenshot |
| ------ | ------ |
| Green arrows: AMCL Particles; Deep Blue Square: Local Mapping; Lighter blue: Global Mapping; Green squares on walls: Laser Scan Particles | <img src="https://github.com/trunc8/udemy_ros_part2/blob/assets/stationary.png" width="700">  |
| move\_base Motion Planner | <img src="https://github.com/trunc8/udemy_ros_part2/blob/assets/move_base.png" width="700">  |
| Dense AMCL Particles with Higher Confidence in Localization | <img src="https://github.com/trunc8/udemy_ros_part2/blob/assets/dense_amcl.png" width="700">  |

### Summary of topics I learnt:
1. How to manipulate the quarternion
2. The *tf* (transform) package and fundamentals
3. Navigation Packages- *move_base*, *gmapping*, and *amcl* with shallow dives into the concepts of each
4. Map-based Navigation Stack- global_planner, local_planner, recovery behaviours, local_costmap, global_costmap
5. Local Path Planner- Dynamic Window Approach
