PDX-License-Identifier: GPL-3.0-only
'''
     Copyright (C) 2020  Haruki Shimotori and Ryuichi Ueda. All right reserved.
'''

import rospy
from std_msgs.msg import String

def cb(message):
    rospy.loginfo("進撃の巨人完結しないで%s",message.data)
if __name__=='__main__':
        rospy.init_node('twice')
        sub = rospy.Subscriber('count_up', String, cb)
        rospy.spin()
      
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
