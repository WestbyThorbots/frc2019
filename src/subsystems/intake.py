#!/usr/bin/python3
"""
intake.py: snag a "cargo"
"""
import wpilib
from wpilib.command import Subsystem

class Intake(Subsystem):
    """
    Intake uses motor to spin green wheel(s) to snag the cargo (ball) that
    has rolled into our "cargo capturing space".
    """
    def __init__(self):
        super().__init__()

        self.intake = wpilib.Talon(6)

    def spin(self):
        self.intake.set(1.0)

    def stop(self):
        self.intake.set(0.0)
