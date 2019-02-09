#!/usr/bin/python3
import math
import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler
from subsystems.drivetrain import DriveTrain
from subsystems.puncher import Puncher
from subsystems.claw import Claw
from subsystems.arm import Arm
from commands.move_arm_with_triggers import MoveArmWithTriggers
from oi import OI

class MyRobot(CommandBasedRobot):
    #Our robot is pieced together in this class.

    def robotInit(self):
        self.drivetrain = DriveTrain(self)
        self.puncher = Puncher()
        self.claw = Claw()
        self.arm = Arm()
        self.oi = OI(self)

    def disabledInit(self):
        return super().disabledInit()

    def disabledPeriodic(self):
        return super().disabledPeriodic()

    def autonomousInit(self):
        return super().autonomousInit()

    def autonomousPeriodic(self):
        Scheduler.getInstance().run()    

    def teleopInit(self):
        return super().teleopInit()

    def teleopPeriodic(self):
        Scheduler.getInstance().run()

    def testInit(self):
        return super().testInit()

    def testPeriodic(self):
        Scheduler.getInstance().run()

if __name__ == "__main__":
    wpilib.run(MyRobot)
