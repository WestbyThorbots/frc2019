from wpilib.command import Command

class CoverHatch(Command):

    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.hatch)

    def initialize(self):
        """Called just before this Command runs the first time"""
        self.robot.hatch.open

    def execute(self):
        """Called repeatedly when this Command is scheduled to run."""
        self.robot.hatch.open

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return self.isTimedOut()

    def end(self):
        """Called once after isFinished returns true"""
        self.robot.hatch.close()

    def interrupted(self):
        """Called when another command which requires one or more of the same
           subsystems is scheduled to run"""
        self.end()