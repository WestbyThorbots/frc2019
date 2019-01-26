from wpilib.command import Command

class DifferentialDriveWithXbox(Command):

    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.drivetrain)

    def initialize(self):
        """Called just before this Command runs the first time"""

    def execute(self):
        """Called repeatedly when this Command is scheduled to run."""
        self.robot.drivetrain.driveXbox0(self.robot.oi.getXbox0())