#!/usr/bin/env python3
"""The cargo launcher subsystem."""

import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Subsystem
from commands.punch import Punch

class Puncher(Subsystem):
    """Puncher subsystem. This is a pneumatic puncher, implemented with
    a double solenoid to fire the puncher."""
    def __init__(self):
        """Assign and save the double solenoid assignment for the puncher."""
        super().__init__()

        self.puncher = DoubleSolenoid(0,7,6)

    def open(self):
        """Open (retract) the puncher."""
        self.puncher.set(DoubleSolenoid.Value.kReverse)

    def close(self):
        """Close (extend) the puncher."""
        self.puncher.set(DoubleSolenoid.Value.kForward)

    def stop(self):
        """Turn off the solenoid."""
        self.puncher.set(DoubleSolenoid.Value.kOff)
