#!/usr/bin/env python3
import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Subsystem

class Puncher(Subsystem):
    """
    Puncher subsystem. This is a pneumatic puncher, Implemented with
    a double solenoid to fire the puncher.
    """
    def __init__(self):
        super().__init__()

        self.puncher = wpilib.DoubleSolenoid(0,2,3)

    def open(self):
        self.puncher.set(DoubleSolenoid.Value.kReverse)

    def close(self):
        self.puncher.set(DoubleSolenoid.Value.kForward)

    def stop(self):
        self.puncher.set(DoubleSolenoid.Value.kOff)