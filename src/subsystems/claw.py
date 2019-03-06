#!/usr/bin/env python3
'''Manipulate the claw on the end of the robot arm.'''

import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Subsystem
from commands.open_claw import OpenClaw
from commands.close_claw import CloseClaw

class Claw(Subsystem):
    """Claw subsystem. This is a pneumatic claw, Implemented with
    a double solenoid to open and close the claw."""
    def __init__(self):
        """Save the double solenoid port assignment to the claw."""
        super().__init__()

        self.claw = wpilib.DoubleSolenoid(0,3,2)

    def open(self):
        """Open the claw."""
        self.claw.set(DoubleSolenoid.Value.kReverse)

    def close(self):
        """Close the claw."""
        self.claw.set(DoubleSolenoid.Value.kForward)

    def stop(self):
        """Turn off the solenoid."""
        self.claw.set(DoubleSolenoid.Value.kOff)
