#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy as np
from std_msgs.msg import UInt16
from sensor_msgs.msg import JointState


class Servo2JointState():
    
    def __init__(self):
        """ Servo2JointState
            
            This node reads the angles in DEGREES from 3 topics called servo0, servo1, servo2 
            and publishes those values to the /joint_input topic used by ros simulator.
            The values of the angles will be constrained to the dimensions of simulated robot 
            used in class.
        """
        """ Data
        """
        self.servo0_angle = 0 #angle must be in degrees
        self.servo1_angle = 0 #angle must be in degrees
        self.servo2_angle = 0 #angle must be in degrees
        self.gripper_angle =0 #angle must be in degrees
        """ Publishers
        """
        self.joint_input_pub = rospy.Publisher('joint_input', JointState, queue_size=10)
        """ Subscribers
        """        
        rospy.Subscriber('servo0', UInt16, self.servo0Cb)
        rospy.Subscriber('servo1', UInt16, self.servo1Cb)
        rospy.Subscriber('servo2', UInt16, self.servo2Cb)
        rospy.Subscriber('servogripper', UInt16, self.gripperCb)
    
        rate = rospy.Rate(10) # 10hz
        state = JointState()
        count=-1.5
        while not rospy.is_shutdown():
            state.name=["base", "arti1", "arti2", "gripper"]
            state.position=[np.deg2rad(self.servo0_angle), np.deg2rad(self.servo1_angle), np.deg2rad(self.servo2_angle),  np.deg2rad(self.gripper_angle)]
            self.joint_input_pub.publish(state)
            rate.sleep()
        
    def servo0Cb(self, data):
        """ This callback is executed when we receive a message in servo0 topic
        """
        lower_limit=0
        higher_limit=180
        sim_lower_limit=-90
        sim_higher_limit=90
        self.servo0_angle=np.interp(data.data,[lower_limit,higher_limit],[sim_lower_limit,sim_higher_limit])

            
    def servo1Cb(self, data):
        """ This callback is executed when we receive a message in servo1 topic
        """
        lower_limit=0
        higher_limit=180
        sim_lower_limit=-90
        sim_higher_limit=90
        self.servo1_angle=np.interp(data.data,[lower_limit,higher_limit],[sim_lower_limit,sim_higher_limit])

    
    def servo2Cb(self, data):
        """ This callback is executed when we receive a message in servo2 topic
        """
        lower_limit=0
        higher_limit=180
        sim_lower_limit=-90
        sim_higher_limit=90
        self.servo2_angle=np.interp(data.data,[lower_limit,higher_limit],[sim_lower_limit,sim_higher_limit])

    def gripperCb(self, data):
        """ This callback is executed when we receive a message in servo2 topic
        """
        lower_limit=0
        higher_limit=180
        sim_lower_limit=-90
        sim_higher_limit=90
        self.gripper_angle=np.interp(data.data,[lower_limit,higher_limit],[sim_lower_limit,sim_higher_limit]) 

if __name__ == "__main__":
    rospy.init_node('servo2jointstate', anonymous=True)
    try:
        Servo2JointState()
    except:
        rospy.logfatal("servo2jointsate.py died")
        pass        

    
    
    
    
