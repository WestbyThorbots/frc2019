#!/usr/bin/env python3
'''Operate the robot's drivetrain.'''

import math

import wpilib
from wpilib import Encoder
from wpilib.command import Subsystem
from wpilib import robotdrive
from wpilib.drive import DifferentialDrive
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
        self.right = wpilib.VictorSP(0)
        self.left = wpilib.VictorSP(1)

        # TODO: switch to DifferentialDrive is the main object that deals with driving
        self.drive = wpilib.RobotDrive(self.left, self.right)
        self.auto_drive = wpilib.drive.DifferentialDrive(self.left, self.right)

        #TODO: These probably will not be the actual ports used
        self.left_encoder = Encoder(2, 3)
        self.right_encoder = Encoder(0, 1)
        
        self.left_encoder.setDistancePerPulse(math.pi*16/360/12)
        self.right_encoder.setDistancePerPulse(math.pi*16/360/12)

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
        #print ("gyro is {}".format(self.gyro.getAngle()))

    def driveAuto(self, left, right):
        self.auto_drive.tankDrive(left, right, True)

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
        return (self.left_encoder.getDistance() + self.right_encoder.getDistance()) / 2

    def getLeftDistance(self):
        return (self.left_encoder.getDistance())

    def getRightDistance(self):
        return (self.right_encoder.getDistance())

    def driveStraight(self, speed):
        #print ("right encoder is: {} left: {}".format(self.right_encoder.getDistance(),
        #    self.left_encoder.getDistance()))
        DistanceDifference = self.getLeftDistance() - self.getRightDistance()
        #print ("left minus right is{}".format (DistanceDifference))
        #print ("gyro is {}".format(self.gyro.getAngle()))

        if DistanceDifference > .2:
            self.driveAuto(speed, 0)
            #print ("too far to the left")
        elif DistanceDifference < -.2:
            self.driveAuto(0, speed)
            #print ("too far to the right")
        else:
            self.driveAuto(-speed, -speed)
            #print ("going straight")
        
    def turn(self, angle, speed):
        if self.gyro.getAngle() > angle:
            self.driveAuto(0, speed)
            print ("I should be turning left, but I'm not.")
        elif self.gyro.getAngle() < angle:
            self.driveAuto(speed, 0)
            print ("I should be turning right, but I'm not.")
            print ("speed is {}.".format(speed))
        else:
            self.driveAuto(0, 0)
            print ("I should be turning, but I think I'm going straight")

