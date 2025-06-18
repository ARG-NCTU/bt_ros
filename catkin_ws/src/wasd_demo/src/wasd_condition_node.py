#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Bool
import Tkinter as tk
import threading
import time

class WASDPublisher(object):
    def __init__(self, root):
        rospy.init_node("wasd_gui_node", anonymous=True)
        self.pubs = {
            'W': rospy.Publisher("w_pressed_success", Bool, queue_size=1),
            'A': rospy.Publisher("a_pressed_success", Bool, queue_size=1),
            'S': rospy.Publisher("s_pressed_success", Bool, queue_size=1),
            'D': rospy.Publisher("d_pressed_success", Bool, queue_size=1),
        }
        self.pressed = {k: False for k in "WASD"}
        for i, key in enumerate("WASD"):
            btn = tk.Button(root, text=key, width=10, height=4)
            btn.grid(row=0, column=i)
            btn.bind('<ButtonPress-1>', lambda e, k=key: self.set_pressed(k, True))
            btn.bind('<ButtonRelease-1>', lambda e, k=key: self.set_pressed(k, False))

        # Background thread 持續發 topic
        self.th = threading.Thread(target=self.loop_pub)
        self.th.setDaemon(True)
        self.th.start()

    def set_pressed(self, key, state):
        self.pressed[key] = state

    def loop_pub(self):
        rate = rospy.Rate(10)  # 10Hz
        while not rospy.is_shutdown():
            for key in "WASD":
                self.pubs[key].publish(Bool(self.pressed[key]))
            rate.sleep()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("WASD GUI (長按可持續發佈)")
    app = WASDPublisher(root)
    root.mainloop()
