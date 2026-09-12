"""
detector_node.py — Water leak detector for the UUV enclosure.

Subscribes to /water_sensor (Bool).
Publishes the result on /leak_status (Bool).
Logs a warning when water is detected.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class WaterLeakDetector(Node):
    def __init__(self):
        super().__init__('water_leak_detector')
        self._pub = self.create_publisher(Bool, '/leak_status', 10)
        self.create_subscription(Bool, '/water_sensor', self._on_reading, 10)
        self.get_logger().info('Leak detector started.')

    def _on_reading(self, msg: Bool):
        if msg.data:
            self.get_logger().warn('WATER LEAK DETECTED!')
        self._pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = WaterLeakDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
