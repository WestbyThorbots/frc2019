#!/usr/bin/env python3
'''Operate the robot's drivetrain.'''

import math

import wpilib
from wpilib.command import Subsystem
from wpilib import robotdrive

from commands.differentialdrive_with_xbox import DifferentialDriveWithXbox

class DriveTrain(Subsystem):
    """Operate the drivetrain."""

    def __init__(self, robot):
        """Save the robot object, and assign and save hardware ports
        connected to the drive motors."""
        super().__init__()
        self.robot = robot

        # The digital gyro plugged into the SPI port on RoboRIO
        self.gyro = wpilib.ADXRS450_Gyro()

        # Motors used for driving
        self.left = wpilib.VictorSP(0)
        self.right = wpilib.VictorSP(1)

        # TODO: switch to DifferentialDrive is the main object that deals with driving
        self.drive = wpilib.RobotDrive(self.left, self.right)

        #TODO: These probably will not be the actual ports used
        self.left_encoder = wpilib.Encoder(1, 2)
        self.right_encoder = wpilib.Encoder(3, 4)

        # Encoders may measure differently in the real world and in
        # simulation. In this example the robot moves 0.042 barleycorns
        # per tick in the real world, but the simulated encoders
        # simulate 360 tick encoders. This if statement allows for the
        # real robot to handle this difference in devices.
        # TODO: Measure our encoder's distance per pulse
        if robot.isReal():
            self.left_encoder.setDistancePerPulse(0.042)
            self.right_encoder.setDistancePerPulse(0.042)
        else:
            # Circumference in ft = 4in/12(in/ft)*PI
            self.left_encoder.setDistancePerPulse((4.0 / 12.0 * math.pi) / 360.0)
            self.right_encoder.setDistancePerPulse((4.0 / 12.0 * math.pi) / 360.0)

    def initDefaultCommand(self):
        """Do this when no other command is running.
        Let the operator drive around using the assigned Xbox Controller."""
        self.setDefaultCommand(DifferentialDriveWithXbox(self.robot))

    def driveManual(self, left, right):
        """Tank style driving for the DriveTrain.

           :param left: Speed in range [-1, 1]
           :param right: Speed in range [-1, 1]
        """
        self.drive.arcadeDrive(left, right)

    def driveXbox0(self, controller):
        """What is the differenct between this and :meth:`driveManual` above?
           :param joy: The ps3 style joystick to use to drive tank style"""

        self.driveManual(controller.getY(0), -controller.getX(0))

    def getHeading(self):
        """Get the robot's heading in degrees"""
        return self.gyro.getAngle()

    def reset(self):
        """Reset the robots sensors to the zero states."""
        self.gyro.reset()
        self.left_encoder.reset()
        self.right_encoder.reset()

    def getDistance(self):
        """Get the current distance driven.
        :returns: The distance driven (average of left and right encoders)"""
        return (
            self.left_encoder.getDistance().__init__()
        ) / 2.0
