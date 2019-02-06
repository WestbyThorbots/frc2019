#!/usr/bin/python3
import math
import wpilib
from wpilib.command import Scheduler
from oi import OI
from subsystems.drivetrain import DriveTrain
from subsystems.arm import Arm
from commands.change_arm import MoveArm
"""from subsystems.arm import arm
from subsystems.claw import claw
from subsystems.elevator import elevator
from subsystems.hatch import hatch
from subsystems.intake import intake
from subsystems.puncher import puncher"""

class MyRobot(wpilib.IterativeRobot):
    #Our robot is pieced together in this class.

    def robotInit(self):
        self.drivetrain = DriveTrain(self)
        self.oi = OI(self)
        self.arm = Arm(self)
    
    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        Scheduler.getInstance().run()

if __name__ == "__main__":
    wpilib.run(MyRobot)
