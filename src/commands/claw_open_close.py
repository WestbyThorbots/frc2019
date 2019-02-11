#!/usr/bin/python3
'''Open and close the claw.'''

from wpilib.command import Command

class ClawOpen(Command):
    '''Do the claw.'''
    def __init__(self, robot):
        '''Save the robot and pull in the claw subsystem.'''
        super().__init__()

        self.robot = robot
        self.requires(self.robot.claw)

    def initialize(self):
        """Called just before this Command runs the first time."""
        self.robot.claw.open()

    def execute(self):
        """Called repeatedly when this Command is scheduled to run.
        Since opening the claw is an atomic action, we do not need
        anything here."""

    def isFinished(self):
        """Make this return true when this Command no longer needs
        to run execute()"""
        return self.isTimedOut()

    def end(self):
        """Called once after isFinished returns true"""
        self.robot.claw.open()

    def interrupted(self):
        """Called when another Command which requires one
        or more of the same subsystems is scheduled to run"""
        self.end()
