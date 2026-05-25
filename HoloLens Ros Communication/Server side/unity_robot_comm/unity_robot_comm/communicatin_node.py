import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Point

class UnityCommunicator(Node):
    def __init__(self):
        super().__init__('unity_communicator')

        self.subscription = self.create_subscription(Point, 'unity_to_ros_topic', self.unity_listener_callback, 10)
        self.publisher_ = self.create_publisher(String, 'ros_to_unity_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Node started successfully!')
    
    def unity_listener_callback(self, msg):
        """this fuction executes whenever Unit sends data to ros"""
        self.get_logger().info(f'X: {msg.x:.2f}, Y: {msg.y:.2f}, Z: {msg.z:.2f}')
    
    def timer_callback(self): 
        """This function executes every second to send a heartbeat to Unity"""
        msg = String()
        msg.data = "heartbeat from ROS server"
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

if __name__=='__main__':
    main()