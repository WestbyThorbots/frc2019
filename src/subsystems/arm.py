#!/usr/bin/env python3
'''Raise and lower the robot's arm.'''

import wpilib
from wpilib.command import Subsystem
from wpilib import Encoder

class Arm(Subsystem):
    """Raise and lower the robot's arm."""
    def __init__(self):
        """Assign ports and save them for use in the move and stop methods."""
        super().__init__()

        self.arm = wpilib.VictorSP(2)
        self.armencoder = Encoder(4, 5)
        self.armencoder.setDistancePerPulse(0.14)

    def move(self, value):
        """Move the arm according to the left and right Xbox
        controller triggers."""
        self.arm.set(value)
        # if self.armencoder.getDistance() < 40:
        #     self.arm.set(value)
        #     if value > 0:
        #         direction = "up"
        #     elif value < 0:
        #         direction = "down"
        #     else:
        #         direction = "stopped"
        #     print("Arm moving", direction, "at", value)

        # print ("Arm angle is " + "%3f" % self.armencoder.getDistance())

    def stop(self):
        """Stop the arm."""
        self.arm.set(0.0)
        #TODO: Change 0.0 to a value that holds the arm at its current value so it doesn't fall.
