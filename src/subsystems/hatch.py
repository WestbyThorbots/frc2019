#!/usr/bin/env python3
import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Subsystem

class Hatch(Subsystem):
    """
    Hatch subsystem. This is a pneumatic hatch subsytstem, Implemented with
    a double solenoid to operate the intake and placement of the hatch panel.
    """
    def __init__(self):
        super().__init__()

        self.hatch = wpilib.DoubleSolenoid(0,4,5)

    def open(self):
        self.hatch.set(DoubleSolenoid.Value.kReverse)

    def close(self):
        self.hatch.set(DoubleSolenoid.Value.kForward)

    def stop(self):
        self.hatch.set(DoubleSolenoid.Value.kOff)