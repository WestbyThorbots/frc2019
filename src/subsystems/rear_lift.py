#!/usr/bin/env python3
'''Manipulate the rear cylinder used for lifting onto the Hab.'''

import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Subsystem

class RearLift(Subsystem):
    """Rear pneumatic lift"""
    def __init__(self):
        super().__init__()

        self.rear_lift = wpilib.DoubleSolenoid(0,3,2)

    def extend(self):
        """Extend the cylinder to lift the robot."""
        self.rear_lift.set(DoubleSolenoid.Value.kReverse)

    def retract(self):
        """Retract the cylinder to lower the robot."""
        self.rear_lift.set(DoubleSolenoid.Value.kForward)

    def stop(self):
        """Turn off the solenoid."""
        self.rear_lift.set(DoubleSolenoid.Value.kOff)
