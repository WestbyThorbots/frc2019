#!/usr/bin/python3

#arm.py controls how the arm moves up and down.

import wpilib
from wpilib.command import Subsystem

class Arm(Subsystem):
    """
    The arm uses a combination of motors and encoders to allow the driver to control it
    manually while also being able to change its height to one of three levels automatically.
    """

    def __init__(self, robot):
        super().__init__()

        self.arm = wpilib.Talon(2)
        self.robot = robot
        print ("Hey we made an arm")

    """def lift(self, controller):
        self.arm.set(controller.getLeftTrigger())

    def lower(self, controller):
        self.arm.set(controller.getRightTrigger())

    def stop(self):
        self.arm.set(0.0)
        #TODO: Change 0.0 to a value that holds the arm at its current value so it doesn't fall.
"""

    def RaiseArm(self, value):
        self.arm.set(0.75)
        print ("In MoveArm value is " + "%2.5f" % value)

    def LowerArm(self, value):
        self.arm.set(-0.75)

    def MoveArm(self, value):
        pass

    def StopArm(self, controller):
        self.arm.set(0)

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

