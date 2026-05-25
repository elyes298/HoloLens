import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Point

ROS_TO_UNITY_TOPIC = 'ros_to_unity_topic'
UNITY_TO_ROS_TOPIC = 'unity_to_ros_topic'


class UnityCommunicator(Node):
    def __init__(self):
        super().__init__('unity_communicator')

        self.subscription = self.create_subscription(Point, UNITY_TO_ROS_TOPIC, self.unity_listener_callback, 10)
        self.publisher_ = self.create_publisher(String, ROS_TO_UNITY_TOPIC, 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Node started successfully!')

    def unity_listener_callback(self, msg):
        """Runs whenever Unity sends a position to ROS."""
        self.get_logger().info(f'X: {msg.x:.2f}, Y: {msg.y:.2f}, Z: {msg.z:.2f}')

    def timer_callback(self):
        """Sends a heartbeat to Unity once per second."""
        msg = String()
        msg.data = 'heartbeat from ROS server'
        self.publisher_.publish(msg)
        self.get_logger().info('sent heartbeat packet to Unity')


def main(args=None):
    rclpy.init(args=args)
    node = UnityCommunicator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down Node')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
