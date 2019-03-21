#!/usr/bin/python3

from commands.drive_straight import DriveStraight
from commands.turn import Turn
from commands.park import Park
from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand

class Left(CommandGroup):

    def __init__(self, robot):
        super().__init__()

        self.addSequential(DriveStraight(robot, 5, .5))
        self.addSequential(Turn(robot, 90, .75))
        self.addSequential(Park(robot))