#!/usr/bin/env python3
import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Subsystem
from commands.punch import Punch

class Puncher(Subsystem):
    """
    Puncher subsystem. This is a pneumatic puncher, Implemented with
    a double solenoid to fire the puncher.
    """
    def __init__(self):
        super().__init__()

        self.puncher = DoubleSolenoid(0,3,2)

    def open(self):
        self.puncher.set(DoubleSolenoid.Value.kReverse)

    def close(self):
        self.puncher.set(DoubleSolenoid.Value.kForward)

    def stop(self):
        self.puncher.set(DoubleSolenoid.Value.kOff)