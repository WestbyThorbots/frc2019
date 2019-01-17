#!/usr/bin/env python3
"""
    This code is designed to assist in the execution of commands specifically
    related to the operation of Team 5903's Thorbot. This code handles the
    programmed aspects of the robot including, but not limited to: Gyroscope,
    Cameras, Limelight, Motors, and Deathrays.
"""

import wpilib
from wpilib.drive import MecanumDrive
from networktables import NetworkTables

class MyRobot(wpilib.SampleRobot):
    # Channels on the roboRIO that the motor controllers are plugged in to
    frontLeftChannel = 1
    rearLeftChannel = 3
    frontRightChannel = 2
    rearRightChannel = 4

    # The channel on the driver station that the joystick is connected to
    xchannel0 = 0

    xchannel1 = 1

    def robotInit(self):
        """Robot initialization function"""
        self.frontLeftMotor = wpilib.VictorSP(self.frontLeftChannel)
        self.rearLeftMotor = wpilib.VictorSP(self.rearLeftChannel)
        self.frontRightMotor = wpilib.VictorSP(self.frontRightChannel)
        self.rearRightMotor = wpilib.VictorSP(self.rearRightChannel)

        # invert the left side motors
      #  self.frontLeftMotor.setInverted(True)

        # you may need to change or remove this to match your robot
       # self.rearLeftMotor.setInverted(True)
       # self.frontRightMotor.setInverted(True)
       # self.rearRightMotor.setInverted(True)

        self.drive = MecanumDrive(
            self.frontLeftMotor,
            self.rearLeftMotor,
            self.frontRightMotor,
            self.rearRightMotor,
        )

        self.drive.setExpiration(0.1)

        self.xbox0 = wpilib.XboxController(self.xchannel0)
        self.xbox1 = wpilib.XboxController(self.xchannel1)

    def operatorControl(self):
        """Runs the motors with Mecanum drive."""

        self.drive.setSafetyEnabled(True)
        while self.isOperatorControl() and self.isEnabled():
            # Use the joystick X axis for lateral movement, Y axis for forward movement, and Z axis for rotation.
            # This sample does not use field-oriented drive, so the gyro input is set to zero.
            self.drive.driveCartesian(
                -self.xbox0.getX(0), -self.xbox0.getY(0), 0
            )

            wpilib.Timer.delay(0.005)  # wait 5ms to avoid hogging CPU cycles


if __name__ == "__main__":
    wpilib.run(MyRobot)
