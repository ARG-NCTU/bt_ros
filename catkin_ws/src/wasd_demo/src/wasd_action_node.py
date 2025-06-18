#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from behavior_tree_msgs.msg import Active, Status

def make_cb(direction, pub):
    def callback(msg):
        if msg.active:
            print("方向: {}".format(direction))
            s = Status()
            s.status = Status.SUCCESS  # 直接回報成功
            s.id = msg.id
            pub.publish(s)
    return callback

if __name__ == "__main__":
    rospy.init_node("wasd_action_node")

    pub_w = rospy.Publisher("w_action_status", Status, queue_size=1)
    pub_a = rospy.Publisher("a_action_status", Status, queue_size=1)
    pub_s = rospy.Publisher("s_action_status", Status, queue_size=1)
    pub_d = rospy.Publisher("d_action_status", Status, queue_size=1)

    rospy.Subscriber("w_action_active", Active, make_cb("front", pub_w))
    rospy.Subscriber("a_action_active", Active, make_cb("left", pub_a))
    rospy.Subscriber("s_action_active", Active, make_cb("back", pub_s))
    rospy.Subscriber("d_action_active", Active, make_cb("right", pub_d))

    rospy.spin()
