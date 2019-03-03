#!/usr/bin/env python3
"""Control the screw jacsk to rais and lower the robot"""

import wpilib
from wpilib.command import Subsystem

class Elevator(Subsystem):
    """Elevator uses two motor controllers to control three motors.
    Two are controlled simultaneously and the other is separate.
    Eventually they'll use two buttons to control each motor controller."""
    def __init__(self):
        '''Assign and save the motor controllers for the front and rear
        screw jacks of the elevator.'''
        super().__init__()

        #self.FrontElevator1 = wpilib.VictorSP(5)
        #self.FrontElevator2 = wpilib.VictorSP(6)
        #self.RearElevator = wpilib.VictorSP(0)

        self.height = 0

    def LiftFront(self):
        '''Lift the front of the robot.'''
        #if self.FrontElevator1.getQuadraturePostion()>4:
        #self.FrontElevator2.follow(self.FrontElevator1, followerType=0)
        self.FrontElevator1.set(1.0)
        self.FrontElevator2.set(1.0)
        #else:
        #self.FrontElevator2.follow(self.FrontElevator1, followerType=0)
        #self.FrontElevator1.set(0.0)

    def LowerFront(self):
        '''Lower the front of the robot.'''
        #self.FrontElevator2.follow(self.FrontElevator1, followerType=0)
        self.FrontElevator1.set(-1.0)
        self.FrontElevator2.set(-1.0)

    def StopFront(self):
        '''Stop the front screwjacks.'''
        #self.FrontElevator2.follow(self.FrontElevator1, followerType=0)
        self.FrontElevator1.set(0.0)

    def LiftRear(self):
        '''Lift the rear of the robot.'''
        self.RearElevator.set(1.0)

    def LowerRear(self):
        '''Lower the rear of the robot.'''
        self.RearElevator.set(-1.0)

    def StopRear(self):
        '''Stop the rear screw jacks.'''
        self.RearElevator.set(0.0)

    def Lift(self):
        '''Lift the robot front and rear simultaneously.'''
        self.LiftFront()
        self.LiftRear()

    def Lower(self):
        '''Lower the front and rear simultaneously.'''
        self.LowerFront()
        self.LowerRear()

    def Stop(self):
        '''Stop both screw jacks.'''
        self.StopFront()
        self.StopRear()

    def LiftLeft(self):
        self.FrontElevator1.set(1.0)

    def LowerLeft(self):
        self.FrontElevator1.set(-1.0)

    def StopLeft(self):
        self.FrontElevator1.set(0.0)

    def LiftRight(self):
        self.FrontElevator2.set(1.0)

    def LowerRight(self):
        self.FrontElevator2.set(-1.0)

    def StopRight(self):
        self.FrontElevator2.set(0.0)
