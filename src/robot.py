#!/usr/bin/python3
import math
import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler
from oi import OI
from subsystems.drivetrain import DriveTrain
from subsystems.puncher import Puncher
#from .subsystems.arm import Arm
#from .subsystems.arm import Arm
#from .subsystems.claw import Claw
#from .subsystems.elevator import Elevator
#from .subsystems.hatch import Hatch
#from .subsystems.intake import Intake
#from .commands.change_arm import MoveArm

class MyRobot(CommandBasedRobot):
    #Our robot is pieced together in this class.

    def robotInit(self):
        self.drivetrain = DriveTrain(self)
        self.puncher = Puncher(self)
        self.oi = OI(self)
        #self.arm = Arm(self)

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
