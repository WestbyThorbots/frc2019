#!/usr/bin/env python3
'''Lift and lower the robot using the front and rear screw jacks.'''

from wpilib.command import Command

class LiftFront(Command):
    '''Lift the front screw jacks.'''

    def __init__(self, robot):
        '''Save the robot object and pull in the elevator subsystem.'''
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
    '''Lift the rear screw jack(s).'''

    def __init__(self, robot):
        '''Save the robot object and pull in the elevator subsystem.'''
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
    '''Lower the front screw jacks.'''

    def __init__(self, robot):
        '''Save the robot object and pull in the elevator subsystem.'''

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
    '''Lower the rear screw jack(s).'''

    def __init__(self, robot):
        '''Save the robot object and pull in the elevator subsystem.'''
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
    '''Raise the front and rear screw jacks.'''

    def __init__(self, robot):
        '''Save the robot object and pull in the elevator subsystem.'''
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
    '''Lower the front and rear screw jacks.'''

    def __init__(self, robot):
        '''Save the robot object and pull in the elevator subsystem.'''
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
    '''Stop the front and rear screw jacks.'''

    def __init__(self, robot):
        '''Save the robot object and pull in the elevator subsystem.'''
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
