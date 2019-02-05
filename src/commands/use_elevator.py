#!/usr/bin/python3
"""
This lifts the robot
"""
from wpilib.command import Command

class LiftFront(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.elevator)

    def initialize(self):
        """ TODO: fill in the missing pieces for initialization. """
        self.robot.elevator.LiftFront

    def execute(self):
        """ TODO: make the lift actually do something. """
        self.robot.elevator.LiftFront

    def isFinished(self):
        """ Return "True" when we are done with this command. """
        return self.isTimedOut()

    def end(self):
        self.robot.elevator.Stop()

    def interrupted(self):
        self.end()

class LiftRear(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.elevator)

        def initialize(self):
            """ TODO: fill in the missing pieces for initialization. """
            self.robot.elevator.LiftRear()

        def execute(self):
            """ TODO: make the lift actually do something. """
            self.robot.elevator.LiftRear()

        def isFinished(self):
            """ Return "True" when we are done with this command. """
            return self.isTimedOut()

        def end(self):
            self.robot.elevator.Stop()

        def interrupted(self):
            self.end()

class LowerFront(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.elevator)

        def initialize(self):
            """ TODO: fill in the missing pieces for initialization. """
            self.robot.elevator.LowerRear()

        def execute(self):
            """ TODO: make the lift actually do something. """
            self.robot.elevator.LowerRear()

        def isFinished(self):
            """ Return "True" when we are done with this command. """
            return self.isTimedOut()

        def end(self):
            self.robot.elevator.Stop()

        def interrupted(self):
            self.end()

class LowerRear(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.elevator)

        def initialize(self):
            """ TODO: fill in the missing pieces for initialization. """
            self.robot.elevator.LowerRear()

        def execute(self):
            """ TODO: make the lift actually do something. """
            self.robot.elevator.LowerRear()

        def isFinished(self):
            """ Return "True" when we are done with this command. """
            return self.isTimedOut()

        def end(self):
            self.robot.elevator.Stop()

        def interrupted(self):
            self.end()

class RaiseBoth(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.elevator)

        def initialize(self):
            """ TODO: fill in the missing pieces for initialization. """
            self.robot.elevator.Lift()

        def execute(self):
            """ TODO: make the lift actually do something. """
            self.robot.elevator.Lift()

        def isFinished(self):
            """ Return "True" when we are done with this command. """
            return self.isTimedOut()

        def end(self):
            self.robot.elevator.Stop()

        def interrupted(self):
            self.end()

class LowerBoth(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.elevator)

        def initialize(self):
            """ TODO: fill in the missing pieces for initialization. """
            self.robot.elevator.Lower()

        def execute(self):
            """ TODO: make the lift actually do something. """
            self.robot.elevator.Lower()

        def isFinished(self):
            """ Return "True" when we are done with this command. """
            return self.isTimedOut()

        def end(self):
            self.robot.elevator.Stop()

        def interrupted(self):
            self.end()

class StopBoth(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.elevator)

        def initialize(self):
            """ TODO: fill in the missing pieces for initialization. """
            self.robot.elevator.Stop()

        def execute(self):
            """ TODO: make the lift actually do something. """
            self.robot.elevator.Stop()

        def isFinished(self):
            """ Return "True" when we are done with this command. """
            return self.isTimedOut()

        def end(self):
            self.robot.elevator.Stop()

        def interrupted(self):
            self.end()