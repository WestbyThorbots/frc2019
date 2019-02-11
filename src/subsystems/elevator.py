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

        self.FrontElevator = wpilib.Spark(6)
        self.RearElevator = wpilib.Spark(7)

    def LiftFront(self):
        '''Lift the front of the robot.'''
        self.FrontElevator.set(1.0)

    def LowerFront(self):
        '''Lower the front of the robot.'''
        self.FrontElevator.set(-1.0)

    def StopFront(self):
        '''Stop the front screwjacks.'''
        self.FrontElevator.set(0.0)

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
