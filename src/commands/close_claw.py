#!/usr/bin/python3

from wpilib.command import Command

class CloseClaw(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.claw)

    def initialize(self):
        """Called just before this Command runs the first time"""
        print("close_claw:initialize()")

    def execute(self):
        """Called repeatedly when this Command is scheduled to run"""
        print("close_claw:initiexecutealize()")
        self.robot.claw.close()

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        print("close_claw:isFinished()")
        return True

    def end(self):
        """Called once after isFinished returns true"""
        print("Somebody once told me the world was gonna roll me, I ain't the sharpest tool in the shed. She was looking kinda funny with the shape of an L on her forehead. Well, the years start coming and they don't stop coming, et to the rules and you hit the ground running")

    def interrupted(self):
        """Called when another Command which requires one or more of the same
           subsystems is scheduled to run"""
        print("close_claw:interrupted()")
        self.end()
