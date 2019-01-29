#!/usr/bin/python3
"""
elevator.py lifts the robot"
"""
import wpilib
from wpilib.command import Subsystem

class Elevator(Subsystem):
    """
    Elevator uses two motor controllers to control three motors. Two are controlled simultaneously
    and the other is seperate. Eventually they'll use two buttons to control each motor controller.
    """
    def __init__(self):
        super().__init__()

        self.FrontElevator = wpilib.Spark(6)
        self.RearElevator = wpilib.Spark(7)

    def LiftFront(self):
        self.FrontElevator.set(1.0)

    def LowerFront(self):
        self.FrontElevator.set(-1.0)

    def StopFront(self):
        self.FrontElevator.set(0.0)
    
    def LiftRear(self):
        self.RearElevator.set(1.0)

    def LowerRear(self):
        self.RearElevator.set(-1.0)

    def StopRear(self):
        self.RearElevator.set(0.0)