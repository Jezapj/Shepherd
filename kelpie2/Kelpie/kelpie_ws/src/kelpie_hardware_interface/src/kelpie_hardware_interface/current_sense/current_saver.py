#!/usr/bin/env python
import numpy as np
import rospy

import rospy
from kelpie.msg import joint_states
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d")
filename = "/home/kelpie2/Kelpie/kelpie_ws/src/kelpie_hardware_interface/src/kelpie_hardware_interface/current_sense/kelpie_current_measurements.csv"

open(filename, "w").close()

def callback(msg):
    global latest_msg 
    latest_msg = msg
    with open(filename, "a") as f:
        f.write(str(latest_msg) + "\n")
      	#rospy.loginfo(f"Wrote message: {latest_msg}")

def timer_function(event):
    global latest_msg
    #rospy.loginfo(f"Saved the latest message: {latest_msg}")

def current_listener():
    # Subscribe to the topic
    rospy.Subscriber("/kelpie/leg_control/currents", joint_states, callback)

    rospy.Timer(rospy.Duration(1), timer_function)

    #rospy.spin()
#if __name__ == '__main__':
    #current_listener()
