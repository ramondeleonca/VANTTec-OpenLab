"""
test_integration.py — Quick integration test for sensor + detector nodes.
Runs both nodes in a single process for 6 seconds, captures all log output
to a file, then exits cleanly.
"""

import threading
import time
import logging

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from std_msgs.msg import Bool

LOG_FILE = "/tmp/uuv_test.log"
results = []


class Sensor(Node):
    def __init__(self):
        super().__init__('sensor')
        self.pub = self.create_publisher(Bool, '/water_sensor', 10)
        self.create_timer(0.5, self.cb)
        self.tick = 0

    def cb(self):
        self.tick += 1
        msg = Bool()
        msg.data = self.tick > 4   # True after 2 seconds (tick 5+)
        self.pub.publish(msg)
        line = f"[sensor] tick={self.tick} -> water_detected={msg.data}"
        results.append(line)


class Detector(Node):
    def __init__(self):
        super().__init__('detector')
        self.pub = self.create_publisher(Bool, '/leak_status', 10)
        self.create_subscription(Bool, '/water_sensor', self.cb, 10)

    def cb(self, msg):
        status = "LEAK!" if msg.data else "ok"
        line = f"[detector] received={msg.data} -> leak_status={status}"
        results.append(line)
        self.pub.publish(msg)


def main():
    rclpy.init()
    sensor = Sensor()
    detector = Detector()

    executor = MultiThreadedExecutor()
    executor.add_node(sensor)
    executor.add_node(detector)

    t = threading.Thread(target=executor.spin, daemon=True)
    t.start()

    time.sleep(6)

    executor.shutdown()
    rclpy.shutdown()

    with open(LOG_FILE, "w") as f:
        f.write("\n".join(results))
        f.write("\nTEST COMPLETE\n")

    print(f"Results written to {LOG_FILE}")
    for line in results:
        print(line)


if __name__ == '__main__':
    main()
