#!/usr/bin/env python3
"""The cargo launcher subsystem."""

import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Subsystem
from commands.lift_front import LiftFront
from commands.lift_rear import LiftRear

class Lift(Subsystem):
    """Puncher subsystem. This is a pneumatic puncher, implemented with
    a double solenoid to fire the puncher."""
    def __init__(self):
        """Assign and save the double solenoid assignment for the puncher."""
        super().__init__()

        #self.lift_front = DoubleSolenoid(0,7,6)
        self.lift_rear = DoubleSolenoid(0,3,2)

    def liftFront(self):
        """Open (retract) the puncher."""
        #self.lift_front.set(DoubleSolenoid.Value.kReverse)

    def lowerFront(self):
        """Close (extend) the puncher."""
        #self.lift_front.set(DoubleSolenoid.Value.kForward)

    def stopFront(self):
        """Turn off the solenoid."""
        #self.lift_front.set(DoubleSolenoid.Value.kOff)

    def liftRear(self):
        """Open (retract) the puncher."""
        self.lift_rear.set(DoubleSolenoid.Value.kReverse)

    def lowerRear(self):
        """Close (extend) the puncher."""
        self.lift_rear.set(DoubleSolenoid.Value.kForward)

    def stop(self):
        """Turn off the solenoid."""
        self.lift_rear.set(DoubleSolenoid.Value.kOff)
