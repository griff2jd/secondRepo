#!/usr/bin/env python
'''
forward.py
Yuren Liang, Kevin Kordish, Josh Griffin
'''
from geometry_msgs.msg import Point
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Twist
"""Example of a ROS2 node using Python's OO features.  The node is
represented as a class.  Sensor messages are stored in instance
variables.
Author: Nathan Sprague
Version: 7/22/2020
"""
import rclpy
import rclpy.node

from geometry_msgs.msg import Point
from geometry_msgs.msg import Vector3

class ForwardNode(rclpy.node.Node):
    
    def __init__(self):
        super().__init__('forward')


        self.move_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        

        thrust = Twist()
        thrust.linear.x = 0.2 #meters/sec   
        self.get_logger().info("THRUSTERS ENGAGED")
        self.move_pub.publish(thrust)

def main():
    rclpy.init()
    forward_node = ForwardNode()
    rclpy.spin(forward_node)

    forward_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
