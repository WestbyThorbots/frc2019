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
        self.Distance = 0.1
        self.Aim = 0.1
        self.min_aim_command = 0.05
        self.steering_adjust = 0.0

    def initialize(self):
        pass

    def execute(self):
        left_speed = 0.0
        right_speed = 0.0

        # tx is Horizontal Offset From Crosshair To Target (-27 degrees to 27 degrees)
        tx = self.table.getEntry("tx")
        # Vertical Offset From Crosshair To Target (-20.5 degrees to 20.5 degrees)
        ty = self.table.getEntry("ty")
        # Skew or rotation (-90 degrees to 0 degrees)
        ts = self.table.getEntry("ts")
        # tv sees if the limelight has a valid target (0 or 1).
        tv = self.table.getEntry("tv")

        x = tx.getDouble(0)
        y = ty.getDouble(0)
        skew = ts.getDouble(0)
        v = tv.getDouble(0)
		
        if v != 1:
            print("Target Not Detected")
            return
        # When the
        if x > 0:
            right_speed = -0.5

        elif x < 0:
            left_speed = -0.5

        else:
            if y > 0:
                right_speed = -0.5
                left_speed = -0.5

            elif y < 0:
                right_speed = 0.5
                left_speed = 0.5

            else:
                right_speed = 0
                left_speed = 0

        print("left: %1.2f" % left_speed, "right: %1.2f" % right_speed)
        self.robot.drivetrain.driveManual(left_speed, right_speed)

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
