#!/usr/bin/python3
"""Cargo intake subsystem."""

import wpilib
from wpilib.command import Subsystem


class Intake(Subsystem):
    """Intake uses motor to spin green wheel(s) to snag the cargo (ball)
    that has rolled into our "cargo capturing space"."""
    def __init__(self):
        """Assign and save the motor controller that operates the intake."""
        super().__init__()

        self.intake = wpilib.VictorSP(3)

    def spin(self):
        """intake cargo"""
        self.intake.set(.5)

    def eject(self):
        """eject cargo"""
        self.intake.set(-.5)

    def stop(self):
        """Stop the intake motors."""
        self.intake.set(0.0)
