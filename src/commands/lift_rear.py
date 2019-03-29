#!/usr/bin/python3

from wpilib.command import Command

class LiftRear(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.rear_lift)

    def initialize(self):
        """Called just before this Command runs the first time"""

    def execute(self):
        """Called repeatedly when this Command is scheduled to run"""
        self.robot.rear_lift.extend()

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return self.isTimedOut()

    def end(self):
        """Called once after isFinished returns true"""
        self.robot.rear_lift.stop()

    def interrupted(self):
        """Called when another Command which requires one or more of the same
           subsystems is scheduled to run"""
        self.end()
