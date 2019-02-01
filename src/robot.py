#!/usr/bin/python3
import math
import wpilib
from wpilib.command import Scheduler
from oi import OI
from subsystems.drivetrain import DriveTrain

class MyRobot(wpilib.IterativeRobot):
    #Our robot is pieced together in this class.

    def robotInit(self):
        self.drivetrain = DriveTrain(self)
        self.oi = OI(self)
    
    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        Scheduler.getInstance().run()

if __name__ == "__main__":
    wpilib.run(MyRobot)
