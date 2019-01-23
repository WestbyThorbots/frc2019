#!/usr/bin/env python3
"""
    This code is designed to assist in the execution of commands specifically
    related to the operation of Team 5903's Thorbot. This code handles the
    programmed aspects of the robot including, but not limited to: Gyroscope,
    Cameras, Limelight, Motors, and Deathrays.
"""

import wpilib
from wpilib.drive import DifferentialDrive

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Init is called once when the robot is turned on."""

        self.efacing = 1
        """efacing is used to invert our controls."""

        self.CarEncoder = wpilib.Encoder(0, 1)
        #self.HatchEncoder = wpilib.Encoder(3, 4)

        self.chooser = wpilib.SendableChooser()
        self.chooser.addObject('cargo', '1')
        self.chooser.addObject('hatch panel', '2')

        self.left = wpilib.VictorSP(0)
        self.right = wpilib.VictorSP(1)
        """Motors used for driving"""

        self.myRobot = DifferentialDrive(self.left, self.right)
        """DifferentialDrive is the main object that deals with driving"""

        self.RotServo = wpilib.Servo(2)
        self.TiltServo = wpilib.Servo(3)
        """Our two servos will rotate (RotServo) and tilt (TiltServo) our
        vision cameras."""

        self.motor1 = wpilib.Talon(5)
        self.motor2 = wpilib.Talon(6)
        """I mostly just added these motor controllers anticipating some sort
        of intake system that uses motors."""

        #self.Punch = wpilib.Solenoid(4)
        self.DPunch = wpilib.DoubleSolenoid(0,1)
        """The punching mechanism for removal of the hatch panels can use a
        DoubleSolenoid or regular Solenoid. The Solenoid only needs the channel
        it's plugged into (4) whereas the Double Solenoid needs the module
        number, forward channel number, and reverse channel order in that
        order."""
        
        self.XBox0 = wpilib.XboxController(0)
        self.XBox1 = wpilib.XboxController(1)
        """Xbox controllers 1 and 2 on the driver station."""

        self.myRobot.setExpiration(0.1)
        """If communication is cut off between the driver station and the robot
        for over 0.1 seconds, the robot will emergency stop."""


    def teleopInit(self):
        """Executed once at the start of teleop mode"""

        self.myRobot.setSafetyEnabled(True)
        """Motor Safety is another version of setExperiation, except motor
        safety is from the WPI Library."""

    def teleopPeriodic(self):
        """Called every 20 ms during teleop"""

        if self.XBox0.getStartButtonPressed():
            self.efacing *= -1
            """This will invert our controls."""

        if self.XBox0.getAButtonPressed():
            self.Punch.set(True)
            print ("Punch is True")
        else:
            self.Punch.set(False)
            #print ("Punch is False")
            """Operates the puncher controlled by a solenoid."""

        if self.XBox0.getBButtonPressed():
            self.DPunch.set(1)
            print ("DPunch is 1")
        else:
            self.DPunch.set(2)
            #print ("DPunch is 2")
            """Operates the puncher controlled by a double solenoid."""

        #if self.XBox0.getAButtonPressed():
        #self.RotServo.setAngle(90)
        #print ("rotated servo 90 degrees")
        #self.myRobot.arcadeDrive(1,0)

        self.myRobot.arcadeDrive(self.XBox0.getY(0)* -self.efacing, self.XBox0.getX(0)* self.efacing)
        """The efacing variable is here to invert our controls. It's negative
        on the Y axis because otherwise it will be inverted incorrectly."""

if __name__ == "__main__":
    wpilib.run(MyRobot)
