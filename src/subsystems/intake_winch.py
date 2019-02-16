#!/usr/bin/python3
"""Cargo intake subsystem."""

import wpilib
from wpilib.command import Subsystem
import ctre

class IntakeWinch(Subsystem):
    """Intake uses motor to spin green wheel(s) to snag the cargo (ball)
    that has rolled into our "cargo capturing space"."""
    def __init__(self):
        """Assign and save the motor controller that operates the intake."""
        super().__init__()

        self.intakewinch = ctre.WPI_TalonSRX(9)

    def lift(self):
        """Lift the intake wheels"""
        self.intakewinch.set(1.0)
    
    def lower(self):
        """Lower the intake wheels"""
        self.intakewinch.set(-1.0)

    def stop(self):
        """Stop the intake motors."""
        self.intakewinch.set(0.0)