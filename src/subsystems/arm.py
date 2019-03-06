#!/usr/bin/env python3
'''Raise and lower the robot's arm.'''

from wpilib.command import Subsystem
from wpilib import Encoder
import ctre

class Arm(Subsystem):
    """Raise and lower the robot's arm."""
    def __init__(self):
        """Assign ports and save them for use in the move and stop methods."""
        super().__init__()

        self.arm = ctre.WPI_TalonSRX(11)
        self.armencoder = Encoder(0, 1)
        self.armencoder.setDistancePerPulse(0.07)

    def move(self, value):
        """Move the arm according to the left and right Xbox
        controller triggers."""
        if self.armencoder.getDistance() > -120:
            self.arm.set(value)
        else:
            self.arm.set(0.05)

        print("Arm angle is " + "%3f" % self.armencoder.getDistance())

    def stop(self):
        """Stop the arm."""
        self.arm.set(0.0)
        #TODO: Change 0.0 to a value that holds the arm at its current value so it doesn't fall.
