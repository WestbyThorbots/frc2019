#!/usr/bin/env python3
import wpilib
from wpilib import DoubleSolenoid
from wpilib.command import Subsystem
from commands.open_claw import OpenClaw
from commands.close_claw import CloseClaw
class Claw(Subsystem):
    """
    Claw subsystem. This is a pneumatic claw, Implemented with
    a double solenoid to open and close the claw.
    """
    def __init__(self):
        super().__init__()

        self.claw = wpilib.DoubleSolenoid(0,0,1)

    def open(self):
        self.claw.set(DoubleSolenoid.Value.kReverse)

    def close(self):
        self.claw.set(DoubleSolenoid.Value.kForward)

    def stop(self):
        self.claw.set(DoubleSolenoid.Value.kOff)
