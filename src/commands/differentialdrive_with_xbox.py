#!/usr/bin/env python3
'''Drive differentially with an Xbox controller.'''

from wpilib.command import Command
from wpilib.xboxcontroller import XboxController

class DifferentialDriveWithXbox(Command):
    '''Drive differentially with an Xbox controller.'''
    def __init__(self, robot):
        '''Save the robot object and pull in the drivetrain subsystem.'''
        super().__init__()

        self.robot = robot
        self.requires(self.robot.drivetrain)

    def initialize(self):
        """Called just before this Command runs the first time"""

    def execute(self):
        """Called repeatedly when this Command is scheduled to run."""
        self.robot.drivetrain.driveManual(self.robot.xbox0.getY(0), -self.robot.xbox0.getX(0))

    def isFinished(self):
        """Make this return true when this Command no longer needs to
        run execute()"""
        return False  # Runs until interrupted

    def end(self):
        """Called once after isFinished returns true"""
        self.robot.drivetrain.driveManual(0, 0)

    def interrupted(self):
        """Called when another command which requires one or more of
        the same subsystems is scheduled to run"""
        self.end()
