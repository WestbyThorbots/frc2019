#!/usr/bin/env python3
"""The cargo launcher subsystem."""

import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Subsystem

class RearPuncher(Subsystem):
    """Puncher subsystem. This is a pneumatic puncher, implemented with
    a double solenoid to fire the puncher."""
    def __init__(self):
        """Assign and save the double solenoid assignment for the puncher."""
        super().__init__()

        self.rearpuncher = DoubleSolenoid(0, 0, 1)

    def open(self):
        """Open (retract) the puncher."""
        self.rearpuncher.set(DoubleSolenoid.Value.kReverse)

    def close(self):
        """Close (extend) the puncher."""
        self.rearpuncher.set(DoubleSolenoid.Value.kForward)

    def stop(self):
        """Turn off the solenoid."""
        self.rearpuncher.set(DoubleSolenoid.Value.kOff)
