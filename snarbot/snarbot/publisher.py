import rclpy
import math
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class Integ():
    def __init__(self):
        self.x = 0
    def integ(self,V):
        self.x += V*0.1
        return self.x
class Wel():
    def __init__(self):
        self.b = 0.1/(0.1+1)
        self.x = 0
    def integ(self,w):
        self.x = self.b*self.x+(1-self.b)*w
        return self.x

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('publisher')
        self.odom = self.create_publisher(Odometry, 'odom', 10)
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.update,
            1)
        self.Integx = Integ()
        self.Integy = Integ()
        self.IntegO = Integ()
        self.Wl = Wel()
        self.Wr = Wel()

    def update(self,msg):
    
        wlt = (2*msg.linear.x/0.033-msg.angular.z*0.287/0.033)/2
        wrt = (2*msg.linear.x/0.033+msg.angular.z*0.287/0.033)/2
        
        wl = self.Wl.integ(wlt)
        wr = self.Wr.integ(wrt)
        
        V = (0.033/2)*(wl+wr)
        ang = (0.033/0.287)*(wr-wl)
        
        x = self.Integx.integ(math.cos(self.IntegO.x)*V)
        y = self.Integy.integ(math.sin(self.IntegO.x)*V)
        z = self.IntegO.integ(ang)
        
        odometry = Odometry()
        odometry.header.frame_id = "odom"
        odometry.header.stamp = self.get_clock().now().to_msg()
        odometry.pose.pose.orientation.z=float(z)
        odometry.pose.pose.position.x=float(x)
        odometry.pose.pose.position.y=float(y)
        self.odom.publish(odometry)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
