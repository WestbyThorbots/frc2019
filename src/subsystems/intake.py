#!/usr/bin/python3
"""Cargo intake subsystem."""

import wpilib
from wpilib.command import Subsystem
import ctre

class Intake(Subsystem):
    """Intake uses motor to spin green wheel(s) to snag the cargo (ball)
    that has rolled into our "cargo capturing space"."""
    def __init__(self):
        """Assign and save the motor controller that operates the intake."""
        super().__init__()

        self.intake = ctre.WPI_TalonSRX(8)

    def spin(self):
        """Spin the intake motors."""
        self.intake.set(.5)

    def stop(self):
        """Stop the intake motors."""
        self.intake.set(0.0)
