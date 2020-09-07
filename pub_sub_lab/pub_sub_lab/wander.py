#!/usr/bin/env python
'''
wander.py
Yuren Liang, Kevin Kordish, Josh Griffin
'''
from geometry_msgs.msg import Point
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Twist
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan

import rclpy
import rclpy.node

from geometry_msgs.msg import Point
from geometry_msgs.msg import Vector3

class WanderNode(rclpy.node.Node):
    
    def __init__(self):
        super().__init__('wander')
        
        self.scan_msg = None

        self.laser_sub = self.create_subscription(LaserScan, '/scan', self.scan_callback, qos_profile_sensor_data)
        self.stop_pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def scan_callback(self, scan_msg):
        self.scan_msg = scan_msg
        
        if self.scan_msg.ranges[0] <= 1:
            self.thrust = Twist()
            self.thrust.linear.x = 0.2
            self.thrust.angular.z = 3.14
            self.stop_pub.publish(self.thrust)
            
        else:
            self.thrust = Twist()
            self.thrust.linear.x = 0.2
            self.thrust.angular.z = 0.0
            self.stop_pub.publish(self.thrust)
        
        

def main():
    rclpy.init()
    wander_node = WanderNode()
    rclpy.spin(wander_node)

    wander_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
