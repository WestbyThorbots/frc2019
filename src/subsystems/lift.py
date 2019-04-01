#!/usr/bin/env python3
import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Subsystem

class Lift(Subsystem):
    def __init__(self):
        super().__init__()

        self.front_lift = DoubleSolenoid(0,6,7)
        self.rear_lift = wpilib.DoubleSolenoid(0,3,2)

    def lift_front(self):
        self.front_lift.set(DoubleSolenoid.Value.kReverse)

    def lift_rear(self):
        self.rear_lift.set(DoubleSolenoid.Value.kForward)

    def stop(self):
        """Turn off the solenoid."""
        self.rear_lift.set(DoubleSolenoid.Value.kOff)
