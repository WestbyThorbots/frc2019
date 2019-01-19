#!/usr/bin/env python3
"""
    This code is designed to assist in the execution of commands specifically
    related to the operation of Team 5903's Thorbot. This code handles the
    programmed aspects of the robot including, but not limited to: Gyroscope,
    Cameras, Limelight, Motors, and Deathrays.
"""

import wpilib
from wpilib.drive import DifferentialDrive

class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        """Robot initialization function"""
        self.efacing = 1
        # object that handles basic drive operations
        self.left = wpilib.VictorSP(0)
        self.right = wpilib.VictorSP(1)

        self.myRobot = DifferentialDrive(self.left, self.right)

        self.servo = wpilib.Servo(2)

        self.myRobot.setExpiration(0.1)

        # joysticks 1 & 2 on the driver station
        self.XBox0 = wpilib.XboxController(0)
        self.XBox1 = wpilib.XboxController(1)

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        if self.XBox0.getStartButtonPressed():
            self.efacing *= -1

        self.myRobot.arcadeDrive(self.XBox0.getY(0)* -self.efacing, self.XBox0.getX(0)* self.efacing)

if __name__ == "__main__":
    wpilib.run(MyRobot)
