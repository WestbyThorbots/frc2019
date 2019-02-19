from wpilib.command import Command
import wpilib
from networktables import NetworkTables

class Park(Command):

    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.drivetrain)

        NetworkTables.initialize(server='10.59.3.2')
        self.table = NetworkTables.getDefault().getTable("limelight")
        self.Distance = -0.1
        self.Aim = -0.1
        self.min_aim_command = 0.05
        self.steering_adjust = 0.0
        self.left_command = 0.0
        self.right_command = 0.0

    def initialize(self):
        pass

    def execute(self):
        tx = self.table.getEntry("tx")
        ty = self.table.getEntry("ty")
        ta = self.table.getEntry("ta")
        ts = self.table.getEntry("ts")

        x = tx.getDouble(0)
        y = ty.getDouble(0)

        heading_error = x
        distance_error = y
		
        if x > 1.0:
	        self.steering_adjust = heading_error - self.min_aim_command
        elif x < 1.0:
            self.steering_adjust = self.Aim*heading_error + self.min_aim_command

        distance_adjust = self.Distance * distance_error

        self.left_command += self.steering_adjust + distance_adjust
        self.right_command -= self.steering_adjust + distance_adjust
        self.robot.drivetrain.driveManual(self.left_command, self.right_command)

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return self.isTimedOut()

    def end(self):
        """Called once after isFinished returns true"""
        pass

    def interrupted(self):
        """Called when another Command which requires one or more of the same
           subsystems is scheduled to run"""
        self.end()
