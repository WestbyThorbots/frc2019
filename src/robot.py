#!/usr/bin/python3
'''robot.py: The "main" line of the code.'''

import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler

from oi import OI

from subsystems.arm import Arm
from subsystems.drivetrain import DriveTrain
from subsystems.hatch import Hatch
from subsystems.intake import Intake
from subsystems.intake_winch import IntakeWinch
from subsystems.lift import Lift
from subsystems.limelight import LimeLight
from subsystems.puncher import Puncher
from subsystems.rear_puncher import RearPuncher

class MyRobot(CommandBasedRobot):
    '''Primary class, the Periodic methods in which are called
    repeatedly by the RoboRIO system service.'''

    def robotInit(self):
        '''Initialize all subsystems.'''
        self.arm = Arm()
        self.drivetrain = DriveTrain(self)
        self.hatch = Hatch()
        self.intake = Intake()
        self.intake_winch = IntakeWinch()
        self.lift = Lift()
        self.limelight = LimeLight()
        self.puncher = Puncher()
        self.rear_puncher = RearPuncher()

        self.front = -1

        self.oi = OI(self)

    def teleopInit(self):
        '''Initialize systems when entering Teleoperated Mode.'''

    def teleopPeriodic(self):
        '''Called approximately every 20ms while in Teleoperated Mode.'''
        Scheduler.getInstance().run()

    def testInit(self):
        '''Initialize systems when entering Test Mode.'''

    def testPeriodic(self):
        '''Called approximately every 20ms while in Test Mode.'''
        Scheduler.getInstance().run()

if __name__ == "__main__":
    '''Kick off the robot code.
    '''
    wpilib.run(MyRobot)
