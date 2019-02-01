#!/usr/bin/python3
"""
arm.py: implement the arm into code.
"""
import wpilib
from wpilib.command import Subsystem

class Arm(Subsystem):
    """
    The arm uses a combination of motors and encoders to allow the driver to control it
    manually while also being able to change its height to one of three levels automatically.
    """

    def __init__(self):
        super().__init__()

        self.arm = wpilib.Talon(9)

    def lift(self):
        self.arm.set(self.speed)

    def lower(self):
        self.arm.set(self.speed)

    def stop(self):
        self.arm.set(0.0)
        #TODO: Change 0.0 to a value that holds the arm at its current value so it doesn't fall.

class Wrist(Subsystem):
    """
    The wrist moves seperate from the arm, but it's in the same file in order to let it stay
    level while the arm is moving. It's just for convience.
    """

    def __init__(self):
        super().__init__()

        self.wrist = wpilib.Talon(10)

        def lift(self):
            self.wrist.set(self.speed)

        def lower(self):
            self.wrist.set(self.speed)

        def stop(self):
            self.wrist.set(0.0)
            #TODO: Change 0.0 to a value that won't let the claw lower WITH CARGO!!

            