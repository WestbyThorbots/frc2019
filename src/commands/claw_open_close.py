#!/usr/bin/python3
from wpilib import XboxController

from wpilib.command import Command

class ClawOpen(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.claw)

    def initialize(self):
        """Called just before this Command runs the first time"""
        self.robot.claw.open()

    def execute(self):
        """Called repeatedly when this Command is scheduled to run"""

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return self.isTimedOut()

    def end(self):
        """Called once after isFinished returns true"""
        self.robot.claw.open()

    def interrupted(self):
        """Called when another command which requires one or more of the same
           subsystems is scheduled to run"""
        self.end()

class ClawClose(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.claw)

    def initialize(self):
        """Called just before this Command runs the first time"""
        self.robot.claw.close()

    def execute(self):
        """Called repeatedly when this Command is scheduled to run"""

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return self.isTimedOut()

    def end(self):
        """Called once after isFinished returns true"""
        self.robot.claw.close()

    def interrupted(self):
        """Called when another command which requires one or more of the same
           subsystems is scheduled to run"""
        self.end()
