"""
sensor_node.py — Simulated water sensor for the UUV enclosure.

Publishes True (water detected) or False (dry) on /water_sensor at 1 Hz.
After 15 seconds it simulates a leak starting.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class WaterSensorSim(Node):
    def __init__(self):
        super().__init__('water_sensor_sim')
        self._pub = self.create_publisher(Bool, '/water_sensor', 10)
        self.create_timer(1.0, self._publish)
        self._tick = 0
        self.get_logger().info('Water sensor simulator started.')

    def _publish(self):
        self._tick += 1
        # Leak starts after 15 seconds
        water_detected = self._tick >= 15
        msg = Bool()
        msg.data = water_detected
        self._pub.publish(msg)
        self.get_logger().info(f'water_sensor: {water_detected}')


def main(args=None):
    rclpy.init(args=args)
    node = WaterSensorSim()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
