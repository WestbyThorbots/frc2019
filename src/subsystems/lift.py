#!/usr/bin/env python3
import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Subsystem

class Lift(Subsystem):
    def __init__(self):
        super().__init__()

        self.front_lift = DoubleSolenoid(0,6,7)
        self.rear_lift = wpilib.DoubleSolenoid(0,2,3)

    def lift_front(self):
        self.front_lift.set(DoubleSolenoid.Value.kReverse)
        print("front lifted")

    def lift_rear(self):
        self.rear_lift.set(DoubleSolenoid.Value.kForward)
        print("rear lifted")

    def lower_rear(self):
        self.rear_lift.set(DoubleSolenoid.Value.kReverse)
        print("rear lowered")

    def lower_front(self):
        self.front_lift.set(DoubleSolenoid.Value.kForward)
        print("front lowered")

    def stop(self):
        """Turn off the solenoid."""
        self.rear_lift.set(DoubleSolenoid.Value.kOff)
